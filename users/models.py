from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    questions_answered = models.ManyToManyField('home.Question')
    correctAnswers = models.IntegerField(default=0)
    wrongAnswers = models.IntegerField(default=0)
    # https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/ - Invaluable Blogs on Many to Many
    # https://medium.com/@yabiz/django-many-to-many-relationship-in-5-steps-a3af448e3702
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            # if img.height > img.width:
            #     output_size = ((img.width / img.height) * 300, 300)
            # else:
            #     output_size = (300, (img.height / img.width) * 300)
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)