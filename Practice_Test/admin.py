# from django.contrib import admin
# from .models import Question, Answer, Quiz, QuizAttempt

# # Register your models here.
# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 2

# class AnswerInline(admin.StackedInline):
#     model = Answer
#     extra = 2

# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('name', 'creator', 'creation', 'possible',)
#     search_fields = ('name', 'creator')
#     inlines = [QuestionInline]

# admin.site.register(Quiz, QuizAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerInline]
#     search_fields = ('question', 'quiz', 'value',)
#     list_display = ('question', 'quiz', 'value',)

# admin.site.register(Question, QuestionAdmin)