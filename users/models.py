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



class StaticContent(models.Model):
    """Stores Information for static pages like About and Study Pages"""

    class Meta:
        abstract = True



class TestDescription(StaticContent):
    """Stores Test Description Information for Study Page"""
    TEST_TYPES = [
        ('ACT', 'ACT'),
        ('SAT', 'SAT'),
        ('GRE', 'GRE'),
    ]
    test_type = models.CharField(max_length=3, choices=TEST_TYPES, default='SAT')
    link = models.CharField(default="Default Link", max_length=1000)
    blurb_1 = models.CharField(default="Default Description", max_length=1000)
    blurb_2 = models.CharField(default="Default Description", max_length=1000)

    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return f'{self.test_type}'



class TeamMember(StaticContent):
    """Stores Team Member information for About Page"""
    title = models.CharField(max_length=20, default="Default Title")
    image = models.ImageField(default='default.jpg', upload_to='team_pics')
    description = models.CharField(default="Default Description", max_length=100)


    def __str__(self):
        """Returns object as string for admin view and database queries"""
        return f'{self.title}'


    def save(self, *args, **kwargs):
        """Overrides save function.
        
        Resizes team member picture before upload.
        """
        super().save()

        img = Image.open(self.image.path)
        output_size = (100, 100)
        img = img.resize(output_size, Image.ANTIALIAS)
        img.save(self.image.path)