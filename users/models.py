from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    """Stores a Profile Object. One per User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    correctAnswers = models.IntegerField(default=0)
    wrongAnswers = models.IntegerField(default=0)
    

    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """Overrides save function.
        
        Resizes profile picture before upload.
        """
        super().save()

        img = Image.open(self.image.path)
        output_size = (100, 100)
        img = img.resize(output_size, Image.ANTIALIAS)
        img.save(self.image.path)