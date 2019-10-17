from django import forms
from django.contrib.auth.models import User
from .models import Question

# https://stackoverflow.com/questions/5423590/django-how-to-build-a-formset-for-a-quiz
# https://github.com/myles/django-quiz/blob/master/forms.py
# https://github.com/tomwalker/django_quiz

# class QuestionForm(forms.ModelForm):

#     class Meta:
#         model = Question
#         fields = ['choices']

#     def __init__(self, *args, **kwargs):
#         super(QuestionForm, self).__init__(*args, **kwargs)
        
#         choices = forms.ModelChoiceField(queryset=self.instance.first.choice_set, widget=forms.RadioSelect())