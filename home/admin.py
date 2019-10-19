from django.contrib import admin

from .models import Question, Choice, QuestionCopy, ChoiceCopy

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class SATQuestion(Question):
    class Meta:
        proxy = True

class SATQuestionAdmin(QuestionAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(test_type='SAT')

class ACTQuestion(Question):
    class Meta:
        proxy = True

class ACTQuestionAdmin(QuestionAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(test_type='ACT')

class GREQuestion(Question):
    class Meta:
        proxy = True

class GREQuestionAdmin(QuestionAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(test_type='GRE')


admin.site.register(Question, QuestionAdmin)
admin.site.register(SATQuestion, SATQuestionAdmin)
admin.site.register(ACTQuestion, ACTQuestionAdmin)
admin.site.register(GREQuestion, GREQuestionAdmin)