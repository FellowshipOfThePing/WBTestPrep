from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from django.contrib import admin


class Question(models.Model):   
    subject = models.CharField(max_length=100)
    TEST_TYPES = [
        ('ACT', 'ACT'),
        ('SAT', 'SAT'),
        ('GRE', 'GRE'),
    ]
    test_type = models.CharField(max_length=3, choices=TEST_TYPES, default='SAT')
    title = models.CharField(max_length=100)
    prompt = models.TextField()
    image = models.ImageField(default=None, upload_to='question_images')
    date_published = models.DateTimeField(default=timezone.now)
    hint = models.TextField(default="There is no hint for this Question")
    orderId = models.IntegerField(default=0)

    def __str__(self):
        return "Q" + str(self.orderId) + " - " + str(self.title)

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'test_type': (self.test_type), 'orderId': (self.orderId)})

    def save(self, *args, **kwargs):
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
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE, default="")
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text



class QuestionCopy(models.Model):   
    profile = models.ForeignKey('users.Profile', related_name='questions_answered', on_delete=models.CASCADE, default="")
    TEST_TYPES = [
        ('ACT', 'ACT'),
        ('SAT', 'SAT'),
        ('GRE', 'GRE'),
    ]
    test_type = models.CharField(max_length=3, choices=TEST_TYPES, default='SAT')
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    prompt = models.TextField()
    image = models.ImageField(default=None, upload_to='question_images')
    date_answered = models.DateTimeField(default=timezone.now)
    hint = models.TextField(default="There is no hint for this Question")
    # Keep track of index related to user, 
    copyId = models.IntegerField(default=0)
    # Keep track of orderId of original version
    originalOrderId = models.IntegerField(default=0)
    userAnswer = models.IntegerField(default=0)
    answeredCorrectly = models.BooleanField(default=False)

    @classmethod
    def create(cls, profile, test_type, subject, title, prompt, image, hint, originalOrderId, answeredCorrectly):
        questionCopy = cls(profile=profile, test_type=test_type, subject=subject, title=title, prompt=prompt, image=image, 
            hint=hint, originalOrderId=originalOrderId, answeredCorrectly=answeredCorrectly)
        return questionCopy
        
    def __str__(self):
        return "Q-Copy" + str(self.copyId) + " - " + str(self.title)

    def get_absolute_url(self):
        return reverse('question-review', kwargs={'username': (self.profile.user.username), 'copyId': (self.copyId)})

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.profile.questions_answered.last():
                self.copyId = self.profile.questions_answered.last().copyId + 1
            else:
                self.copyId = 1

        super(QuestionCopy, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)



class ChoiceCopy(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey('QuestionCopy', related_name='choices', on_delete=models.CASCADE, default="")
    correct = models.BooleanField(default=False)

    @classmethod
    def create(cls, text, question, correct):
        choiceCopy = cls(choice_text=text, question=question, correct=correct)
        return choiceCopy

    def __str__(self):
        return self.choice_text