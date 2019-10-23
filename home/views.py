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
from .models import Question, QuestionCopy, Choice, ChoiceCopy
from django.urls import reverse


def startpage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'home/startpage.html')

def about(request):
    return render(request, 'home/about.html')


@login_required
def QuestionView(request, test_type, orderId):
    try:
        question = Question.objects.get(test_type=test_type, orderId=orderId)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'question': Question.objects.filter(test_type=test_type, orderId=orderId).first(),
        'nextQuestion': Question.objects.filter(test_type=test_type, orderId=orderId).first().orderId + 1
    }

    return render(request, 'home/question_detail.html', context)


@login_required
def SubmitAnswer(request, test_type, orderId):
    question = get_object_or_404(Question, test_type=test_type, orderId=orderId)
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
            correct = True
        else:
            student.wrongAnswers += 1
            student.save()
            correct = False
        newChoiceList = question.choices.all()
        questionCopy = QuestionCopy.create(request.user.profile, question.test_type, question.subject, question.title, question.title, question.image, question.hint,
            question.orderId, correct)
        questionCopy.save()
        for i, choice in enumerate(newChoiceList):
            if choice == selected_choice:
                answerIndex = i + 1
            newChoice = ChoiceCopy.create(choice.choice_text, questionCopy, choice.correct)
            newChoice.save()
        questionCopy.userAnswer = answerIndex
        questionCopy.save()
        student.questions_answered.add(questionCopy)
        return HttpResponseRedirect(reverse('question-result', kwargs={'test_type': question.test_type, 'orderId': questionCopy.originalOrderId}))


@login_required
def QuestionResultView(request, test_type, orderId):
    question = get_object_or_404(Question, test_type=test_type, orderId=orderId)
    answer = request.user.profile.questions_answered.last().userAnswer
    solved = False
    for i, choice in enumerate(question.choices.all()):
        if choice.correct and (i == answer - 1):
            solved = True
    context = {
        'question': question,
        'nextQuestion': question.orderId + 1,
        'lastQuestionId': Question.objects.filter(test_type=test_type).last().orderId,
        'answer': answer,
        'solved': solved
    }
    return render(request, 'home/question_result.html', context)


@login_required
def QuestionReview(request, username, copyId):
    userProfile = User.objects.filter(username=username).first().profile
    questionCopy = get_object_or_404(QuestionCopy, profile=userProfile, copyId=copyId)
    context = {
        'question': questionCopy,
        'nextQuestion': questionCopy.copyId + 1,
        'lastQuestion': questionCopy.copyId - 1
    }
    return render(request, 'home/question_review.html', context)