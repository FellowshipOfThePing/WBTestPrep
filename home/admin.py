from django.contrib import admin

from .models import Question, Choice, QuestionCopy, ChoiceCopy

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# class ChoiceCopyInline(admin.TabularInline):
#     model = ChoiceCopy

# class QuestionCopyAdmin(admin.ModelAdmin):
#     inlines = [ChoiceCopyInline]

# admin.site.register(QuestionCopy, QuestionCopyAdmin)