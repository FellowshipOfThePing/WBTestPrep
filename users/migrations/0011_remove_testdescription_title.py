# Generated by Django 2.2.6 on 2019-11-06 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191106_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdescription',
            name='title',
        ),
    ]
