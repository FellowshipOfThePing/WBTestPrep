# Generated by Django 2.2.6 on 2019-10-19 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191018_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questioncopy',
            old_name='date_published',
            new_name='date_answered',
        ),
    ]