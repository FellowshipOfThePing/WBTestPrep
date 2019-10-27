from django.contrib import admin
from django.apps import apps
from .models import Profile


QuestionCopy = apps.get_model('home', 'QuestionCopy')
ChoiceCopy = apps.get_model('home', 'ChoiceCopy')


class QuestionCopyInline(admin.TabularInline):
    model = QuestionCopy
    exclude = ['prompt', 'image', 'hint', 'date_answered']
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    inlines = [QuestionCopyInline]

admin.site.register(Profile, ProfileAdmin)