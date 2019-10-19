from django.contrib import admin
from .models import Profile
from django.apps import apps

QuestionCopy = apps.get_model('home', 'QuestionCopy')
ChoiceCopy = apps.get_model('home', 'ChoiceCopy')

# class ChoiceCopyInline(admin.TabularInline):
#     model = ChoiceCopy

# class QuestionCopyAdmin(admin.ModelAdmin):
#     inlines = [ChoiceCopyInline]

# admin.site.register(QuestionCopy, QuestionCopyAdmin)

class QuestionCopyInline(admin.TabularInline):
    model = QuestionCopy
    exclude = ['subject', 'prompt', 'image', 'hint', 'date_answered']
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    inlines = [QuestionCopyInline]

admin.site.register(Profile, ProfileAdmin)