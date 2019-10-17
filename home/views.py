from django.views.generic import DetailView, FormView
from django.views.generic.edit import FormMixin
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from users.models import Profile
from .models import Question
# from .forms import QuestionForm


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'home/home.html')


# https://docs.djangoproject.com/en/2.2/topics/class-based-views/mixins/#using-formmixin-with-detailview
    
class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    # form = QuestionForm

    def add_current_question(self, request):
        self.request.user.profile.questions_answered.add(self.get_object())

    def get(self, request, *args, **kwargs):
        self.add_current_question(request)
        return super(QuestionDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nextQuestion'] = self.get_object().id + 1
        return context