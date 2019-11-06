from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Question(models.Model):  
    """Question to be answered, with results stored as a copy in user profile (See QuestionCopy Class)"""

    # All Possible Subjects and Test_types, stored for reference in model fields below
    SUBJECTS = {
        ('Math', 'Math'),
        ('Reading', 'Reading'),
        ('Science', 'Science'),
    }
    TEST_TYPES = [
        ('ACT', 'ACT'),
        ('SAT', 'SAT'),
        ('GRE', 'GRE'),
    ]

    # Filterable model attributes
    subject = models.CharField(max_length=7, choices=SUBJECTS, default='Math')
    test_type = models.CharField(max_length=3, choices=TEST_TYPES, default='SAT')

    # Content to be displayed in Question views
    title = models.CharField(max_length=100)
    prompt = models.TextField()
    image = models.ImageField(default=None, upload_to='question_images')
    hint = models.TextField(default="There is no hint for this Question")

    # Ordering information
    orderId = models.IntegerField(default=0)
    date_published = models.DateTimeField(default=timezone.now)


    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return "Q" + str(self.orderId) + " - " + str(self.title)


    def get_absolute_url(self):
        """Returns URL"""
        return reverse('question-detail', kwargs={'test_type': (self.test_type), 'orderId': (self.orderId)})


    def save(self, *args, **kwargs):
        """Overrides save function.
        
        When Question is first added, increment orderId based on orderId of most recently created instance (filtered based on test_type).
        If its the first instance of the test_type, default orderId to 1.

        Also resizes uploaded image to fit standard 500 x 500 pixel size. 
        """
        if self._state.adding:
            last_id = Question.objects.filter(test_type=self.test_type).aggregate(largest=models.Max('orderId'))['largest']
            if last_id is not None:
                self.orderId = last_id + 1
            else:
                self.orderId = 1

        super(Question, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Choice(models.Model):
    """Choice to be added to Question instance. Shares a many-to-one relationship with Question Instance."""

    # Content to be displayed in Question views
    choice_text = models.CharField(max_length=200)

    # Relationship key
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE, default="")

    # Tracks which choice(s) are correct answers. Typically 1-2 per question.
    correct = models.BooleanField(default=False)


    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return self.choice_text



class QuestionCopy(models.Model):  
    """Represents a copy of a Question instance.
    
    Copies most attributes from original Question instance, to be stored for review and reference by the user.

    Also used to track user statistics, to be displayed on 'stats' or 'profile' pages.
    """ 

    # Relationship key
    profile = models.ForeignKey('users.Profile', related_name='questions_answered', on_delete=models.CASCADE, default="")
    
    # All Possible Subjects and Test_types, stored for reference in model fields below
    TEST_TYPES = [
        ('ACT', 'ACT'),
        ('SAT', 'SAT'),
        ('GRE', 'GRE'),
    ]
    SUBJECTS = {
        ('Math', 'Math'),
        ('Reading', 'Reading'),
        ('Science', 'Science'),
    }

    # Filterable model attributes
    test_type = models.CharField(max_length=3, choices=TEST_TYPES, default='SAT')
    subject = models.CharField(max_length=7, choices=SUBJECTS, default='Math')

    # Content to be displayed in Question views
    title = models.CharField(max_length=100)
    prompt = models.TextField()
    image = models.ImageField(default=None, upload_to='question_images')
    hint = models.TextField(default="There is no hint for this Question")

    # ID to track index related to user, increments with every new instance
    copyId = models.IntegerField(default=0)

    # ID to track orderId of copied Question instance, used to link back to original question for retry/review
    originalOrderId = models.IntegerField(default=0)

    # Tracks user answer index (in list of choices) and correctness
    userAnswer = models.IntegerField(default=0)
    answeredCorrectly = models.BooleanField(default=False)

    # Info to track user statistics both over time (up until this instance)
    date_answered = models.DateTimeField(default=timezone.now)
    
    numberCorrectGeneral = models.IntegerField(default=0)
    numberWrongGeneral = models.IntegerField(default=0)
    currentGeneralAccuracy = models.FloatField(default=0.0)

    numberCorrectOfTestType = models.IntegerField(default=0)
    numberWrongOfTestType = models.IntegerField(default=0)
    currentTestAccuracy = models.FloatField(default=0.0)

    numberCorrectOfSubjectType = models.IntegerField(default=0)
    numberWrongOfSubjectType = models.IntegerField(default=0)
    currentSubjectAccuracy = models.FloatField(default=0.0)


    @classmethod
    def create(cls, profile, test_type, subject, title, prompt, image, hint, originalOrderId):
        """Alternative to overriding __init__ method, as advised against in Django documentation.
        
        Arguments represent attributes to be copied from original Question instance.

        Any missing attributes are either instantiated in the save() method, or in the SumbitAnswer View function.
        """
        questionCopy = cls(profile=profile, test_type=test_type, subject=subject, title=title, prompt=prompt, image=image, 
            hint=hint, originalOrderId=originalOrderId)
        return questionCopy
        

    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return "Q-Copy" + str(self.copyId) + " - " + str(self.title)


    def get_absolute_url(self):
        """Returns URL"""
        return reverse('question-review', kwargs={'username': (self.profile.user.username), 'copyId': (self.copyId)})


    def save(self, *args, **kwargs):
        """Overrides save function.
        
        Adds Attributes through incrementation:
            copyId
            numberCorrectOfType
            numberWrongOfType
        """
        # When QuestionCopy is first added, increment copyId based on copyId of most recently created instance.
        # Very similar to OrderId incrementation in Question Model, without filtering by test_type.
        if self._state.adding:
            if self.profile.questions_answered.last():
                self.copyId = self.profile.questions_answered.last().copyId + 1

            # If its the first instance (first question answered by user), default copyId to 1.
            else:
                self.copyId = 1

            # Saves numberCorrectOfType and numberWrongOfType to reflect user answer accuracy up to the point of this question being answered.
            lastQuestion = self.profile.questions_answered.last()
            lastQuestionOfTestType = self.profile.questions_answered.filter(test_type=self.test_type).last()
            lastQuestionOfSubjectType = self.profile.questions_answered.filter(test_type=self.test_type, subject=self.subject).last()

            if lastQuestion:
                self.numberCorrectGeneral = lastQuestion.numberCorrectGeneral
                self.numberWrongGeneral = lastQuestion.numberWrongGeneral

            if lastQuestionOfTestType:
                self.numberCorrectOfTestType = lastQuestionOfTestType.numberCorrectOfTestType
                self.numberWrongOfTestType = lastQuestionOfTestType.numberWrongOfTestType
           
            if lastQuestionOfSubjectType:
                self.numberCorrectOfSubjectType = lastQuestionOfSubjectType.numberCorrectOfSubjectType
                self.numberWrongOfSubjectType = lastQuestionOfSubjectType.numberWrongOfSubjectType


        super(QuestionCopy, self).save(*args, **kwargs)



class ChoiceCopy(models.Model):
    """Choice to be added to QuestionCopy instance. Shares a many-to-one relationship with QuestionCopy Instance.
    
    List of ChoiceCopy objects is copied from original Question instance every time a new QuestionCopy is created.
    """

    # Content to be displayed in Question views
    choice_text = models.CharField(max_length=200)

    # Relationship Key
    question = models.ForeignKey('QuestionCopy', related_name='choices', on_delete=models.CASCADE, default="")

    # Tracks which choice(s) are correct answers. Typically 1-2 per question.
    correct = models.BooleanField(default=False)


    @classmethod
    def create(cls, text, question, correct):
        """Alternative to overriding __init__ method, as is advised against in Django documentation.
        
        Arguments represent attributes to be copied from original Question instance's Choices.
        """
        choiceCopy = cls(choice_text=text, question=question, correct=correct)
        return choiceCopy


    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return self.choice_text