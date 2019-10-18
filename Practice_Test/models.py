# from django.db import models
# from django.utils import timezone
# from django.urls import reverse
# from PIL import Image
# from django.contrib.auth.models import User
# from django.contrib import admin


# class Quiz(models.Model):
#     name = models.CharField(max_length=255)
#     creation = models.DateField(auto_now_add=True)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     def possible(self):
#         total = 0
#         for question in self.question_set.all():
#             question.save()
#             total += question.value
#         return total

    
# class Question(models.Model):
#     question = models.CharField(max_length=255)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     creation = models.DateField(auto_now_add=True)
#     value = models.IntegerField(default=1)

#     def __str__(self):
#         return self.question


# class Answer(models.Model):
#     answer = models.CharField(max_length=255)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)


# class QuizAttempt(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)

#     # def score(self):
#     #     total = 0
#     #     for question in self.question_set.all():
#     #         question.save()
#     #         total += question.value
#     #     return total

# class QuestionAttempt(models.Model):
#     attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     response = models.ForeignKey(Answer, on_delete=models.CASCADE)




