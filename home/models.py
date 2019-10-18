from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from django.contrib import admin


class Question(models.Model):   
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    prompt = models.TextField()
    image = models.ImageField(default=None, upload_to='question_images')
    date_published = models.DateTimeField(default=timezone.now)
    hint = models.TextField(default="There is no hint for this Question")
    # userAnswer = models.IntegerField(default=0)

    def __str__(self):
        return "Q" + str(self.pk - 7) + " - " + str(self.title)

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': (self.pk)})

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            # if img.height > img.width:
            #     output_size = ((img.width / img.height) * 300, 300)
            # else:
            #     output_size = (300, (img.height / img.width) * 300)
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE, default="")
    correct = models.BooleanField(default=False)


    def __str__(self):
        return self.choice_text