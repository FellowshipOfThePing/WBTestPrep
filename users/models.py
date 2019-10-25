from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# One profile for each user (this way we don't have to override the User Model)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    correctAnswers = models.IntegerField(default=0)
    wrongAnswers = models.IntegerField(default=0)
    # https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/ - Invaluable Blogs on Many to Many
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        output_size = (100, 100)
        img = img.resize(output_size, Image.ANTIALIAS)
        img.save(self.image.path)


# One for each possible test/subject combination. Created when profile is first saved.
# class HistoryRecord(models.Model):
#     profile = models.ForeignKey('Profile', related_name='history', on_delete=models.CASCADE, default="")
#     TEST_TYPES = [
#         ('ACT', 'ACT'),
#         ('SAT', 'SAT'),
#         ('GRE', 'GRE'),
#     ]
#     test_type = models.CharField(max_length=3, choices=TEST_TYPES, default='SAT')
#     SUBJECTS = [
#         ('Reading', 'Reading'),
#         ('Math', 'Math'),
#         ('Science', 'Science'),
#     ]
#     subject = models.CharField(max_length=3, choices=SUBJECTS, default='Reading')


# # One for each question submitted. Keeps track of user progress, filtered by test type and subject
# class HistoryItem(models.Model):
#     historyRecord = models.ForeignKey('HistoryRecord', related_name='items', on_delete=models.CASCADE, default="")
#     date = models.DateTimeField(default=timezone.now)
#     currentAccuracy = models.FloatField(default=0.0)