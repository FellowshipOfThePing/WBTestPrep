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

def study(request, test_type):
    newQuiz = request.user.profile.questions_answered.last().originalOrderId + 1
    if newQuiz is None:
        newQuiz = 1
    context = {
        'test_type': test_type,
        'newQuiz': newQuiz
    }
    return render(request, 'home/study.html', context)





def stats(request, test_type, subject):
    # Default Iterables
    TEST_TYPES = ['ALL', 'SAT', 'ACT', 'GRE']
    SUBJECTS = ['Math', 'Reading', 'Science', 'English', 'Quantitative', 'Verbal']

    # Setting Iterables
    if test_type == 'ALL':
        questions = request.user.profile.questions_answered.all()
    elif test_type == 'SAT':
        questions = request.user.profile.questions_answered.filter(test_type=test_type).all()
        SUBJECTS = ['Math', 'Reading']
    elif test_type == 'ACT':
        questions = request.user.profile.questions_answered.filter(test_type=test_type).all()
        SUBJECTS = ['Science', 'English']
    else:
        questions = request.user.profile.questions_answered.filter(test_type=test_type).all()
        SUBJECTS = ['Quantitative', 'Verbal']


    # ------- Filtering by Test ------- #
    by_test = {
        # Answer Accuracy (Pie)
        'questionsCorrect': len(questions.filter(answeredCorrectly=True).all()),
        'questionsWrong': len(questions.filter(answeredCorrectly=False).all()),

        # Subject Distribution (Bar)
        'subjectDistribution': [len(questions.filter(subject=s).all()) for s in SUBJECTS],

        # Accuracy Over Time (Line)
        'improvementDates': [question.date_answered for question in questions],
        'improvementNodes': [question.currentUserAccuracy for question in questions]
    }


    # ------- Filtering by Subject ------- #
    questionsBySubject = questions.filter(subject=subject).all()

    by_subject = {
        # Total Accuracy (Pie)
        'questionsCorrect': len(questionsBySubject.filter(answeredCorrectly=True).all()),
        'questionsWrong': len(questionsBySubject.filter(answeredCorrectly=False).all()),

        # Accuracy Over Time (Line)
        'improvementDates': [question.date_answered for question in questionsBySubject],
        'improvementNodes': [question.currentUserAccuracy for question in questionsBySubject]

        # Recommendations (Placeholder for Now) (Bar)
    }

    test_dict = {
        'ALL': ['Math', 'Reading', 'Science', 'English', 'Quantitative', 'Verbal'],
        'SAT': ['Math', 'Reading'],
        'ACT': ['Science', 'English'],
        'GRE': ['Quantitative', 'Verbal']
    }

    question_info = {
        "all_subjects": SUBJECTS
    }

    context = {
        "test_type": test_type,
        "subject": subject,
        "by_test": by_test,
        "by_subject": by_subject,
        "all_subjects": SUBJECTS,
        "test_dict": test_dict
    }


    return render(request, 'home/stats.html', context)






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
    # Get Original Version of Question Answered
    question = get_object_or_404(Question, test_type=test_type, orderId=orderId)

    # Retrieve answer submitted, if none, return 404
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'home/question_detail.html', 
        {
            'question': question,
            'error_message': 'You didn\'t selection an answer',
        })

    
    # If submission is successful
    else:
        student = request.user.profile

        # copy origin Question to store in profile.questions_answered
        newChoiceList = question.choices.all()
        questionCopy = QuestionCopy.create(request.user.profile, question.test_type, question.subject, question.title, question.title, question.image, question.hint,
            question.orderId)
        questionCopy.save()

        # Modify user profile fields to reflect new question submission
        if selected_choice.correct:
            student.correctAnswers += 1
            student.save()
            questionCopy.answeredCorrectly = True
            questionCopy.numberCorrectOfType += 1
        else:
            student.wrongAnswers += 1
            student.save()
            questionCopy.answeredCorrectly = False
            questionCopy.numberWrongOfType += 1

        # Copy original question choices to store in questionCopy foreignkey
        for i, choice in enumerate(newChoiceList):
            if choice == selected_choice:
                answerIndex = i + 1
            newChoice = ChoiceCopy.create(choice.choice_text, questionCopy, choice.correct)
            newChoice.save()

        # Modify questionCopy userAccury fields
        questionCopy.userAnswer = answerIndex
        numberRight = questionCopy.numberCorrectOfType
        numberWrong = questionCopy.numberWrongOfType
        questionCopy.currentUserAccuracy = 100 * (numberRight / (numberRight + numberWrong))
        questionCopy.save()
        student.questions_answered.add(questionCopy)

        # return result view
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