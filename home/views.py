from django.views.generic import DetailView, FormView
from django.views.generic.edit import FormMixin
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.contrib import messages
from users.models import Profile
from .models import Question
# from .forms import QuestionForm
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'home/home.html')

# https://docs.djangoproject.com/en/2.2/topics/class-based-views/mixins/#using-formmixin-with-detailview
    
# class QuestionDetailView(LoginRequiredMixin, DetailView):
#     model = Question
#     form = QuestionForm

#     def add_current_question(self, request):
#         self.request.user.profile.questions_answered.add(self.get_object())

#     def get(self, request, *args, **kwargs):
#         self.add_current_question(request)
#         return super(QuestionDetailView, self).get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
        
#         return super(QuestionDetailView, self).post(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['nextQuestion'] = self.get_object().id + 1
#         return context

@login_required
def QuestionView(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'question': Question.objects.filter(pk=pk).first(),
        'nextQuestion': Question.objects.filter(pk=pk).first().id + 1
    }

    return render(request, 'home/question_detail.html', context)

@login_required
def SubmitAnswer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    request.user.profile.questions_answered.add(question)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'home/question_detail.html', 
        {
            'question': question,
            'error_message': 'You didn\'t selection an answer',
        })
    else:
        student = request.user.profile
        if selected_choice.correct:
            student.correctAnswers += 1
            student.save()
        else:
            student.wrongAnswers += 1
            student.save()
        return HttpResponseRedirect(reverse('question-result', kwargs={'pk': pk}))


@login_required
def QuestionResultView(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,
        'nextQuestion': question.id + 1
    }
    return render(request, 'home/question_result.html', context)