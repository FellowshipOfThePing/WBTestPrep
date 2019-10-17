# from django import forms
# from django.contrib.auth.models import User


# class QuizForm(forms.Form):
#     choices = forms.ModelChoiceField(queryset=)











# # class QuizForm(forms.Form):
    
# #     def __init__(self, questions, *args, **kwargs):
# #         self.questions = questions
# #         for question in questions:
# #             field_name = "question_%d" % question.pk
# #             choices = []
# #             for answer in question.answer_set().all():
# #                 choices.append((answer.pk, answer.answer,))
# #             ## May need to pass some initial data, etc:
# #             field = forms.ChoiceField(label=question.question, required=True, 
# #                                       choices=choices, widget=forms.RadioSelect)
# #         return super(QuizForm, self).__init__(data, *args, **kwargs)


# #     # def save(self):
# #         ## Loop back through the question/answer fields and manually
# #         ## update the Attempt instance before returning it.

