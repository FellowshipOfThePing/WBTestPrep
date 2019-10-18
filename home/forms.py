# from django import forms
# from django.contrib.auth.models import User
# from .models import Question

# # https://stackoverflow.com/questions/5423590/django-how-to-build-a-formset-for-a-quiz
# # https://github.com/myles/django-quiz/blob/master/forms.py
# # https://github.com/tomwalker/django_quiz

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         exclude = ('subject',)
        
#     def __init__(self, question, *args, **kwargs):
#         super(QuestionForm, self).__init__(*args, **kwargs)
#         self.fields['choices'] = forms.ModelChoiceField(queryset=question.choices, widget=forms.RadioSelect())