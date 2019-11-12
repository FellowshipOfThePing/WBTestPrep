# Generated by Django 2.2.6 on 2019-10-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20191024_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questioncopy',
            old_name='currentUserAccuracy',
            new_name='currentSubjectAccuracy',
        ),
        migrations.RenameField(
            model_name='questioncopy',
            old_name='numberCorrectOfType',
            new_name='numberCorrectOfSubjectType',
        ),
        migrations.RenameField(
            model_name='questioncopy',
            old_name='numberWrongOfType',
            new_name='numberCorrectOfTestType',
        ),
        migrations.AddField(
            model_name='questioncopy',
            name='currentTestAccuracy',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='questioncopy',
            name='numberWrongOfSubjectType',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questioncopy',
            name='numberWrongOfTestType',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('Science', 'Science'), ('Math', 'Math'), ('Reading', 'Reading')], default='Math', max_length=7),
        ),
        migrations.AlterField(
            model_name='questioncopy',
            name='subject',
            field=models.CharField(choices=[('Science', 'Science'), ('Math', 'Math'), ('Reading', 'Reading')], default='Math', max_length=7),
        ),
    ]