from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile



def register(request):
    # If request is a post request, create a user with the info in that post request
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Save form info
            form.save()
            # get the username data
            username = form.cleaned_data.get('username')
            # return a User Created message,
            messages.success(request, f'Your account has been created! You are now able to log in')
            # redirect to the home page
            return redirect('login') 
    # If request is not a post request, fill in the form and redirect back to registration
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request, test_type):
    TEST_TYPES = ['ALL', 'SAT', 'ACT', 'GRE']
    userProfile = Profile.objects.filter(user=request.user).first()
    # Setting Iterables
    if test_type == 'ALL':
        questions = userProfile.questions_answered.all().order_by("-copyId")
    else:
        questions = userProfile.questions_answered.filter(test_type=test_type).all().order_by("-copyId")

    test_dict = {
        'ALL': ['Math', 'Reading', 'Science', 'English', 'Quantitative', 'Verbal'],
        'SAT': ['Math', 'Reading'],
        'ACT': ['Science', 'English'],
        'GRE': ['Quantitative', 'Verbal']
    }

    by_test = {
        # Answer Accuracy (Pie)
        'questionsCorrect': len(questions.filter(answeredCorrectly=True).all()),
        'questionsWrong': len(questions.filter(answeredCorrectly=False).all()),

        # Subject Distribution (Bar)
        'subjectDistribution': [len(questions.filter(subject=s).all()) for s in test_dict[test_type]],

        # Accuracy Over Time (Line)
        'improvementDates': [question.date_answered for question in questions],
        'improvementNodes': [question.currentUserAccuracy for question in questions]
    }

    context = {
        'questions': questions[:3],
        'by_test': by_test,
        'all_tests': TEST_TYPES,
        'test_type': test_type
        # 'accuracy': accuracy,
        # 'test_distribution': test_distribution,
        # 'subject_distribution': subject_distribution,
    }

    return render(request, 'users/profile.html', context)



# @login_required
# def profileQuestionHistory(request, test_type):
#     userProfile = Profile.objects.filter(user=request.user).first()
#     questions = userProfile.questions_answered.filter(test_type=test_type).order_by("copyId")
#     accuracy = {
#         "correctAnswers": len(questions.filter(answeredCorrectly=True)),
#         "wrongAnswers": len(questions.filter(answeredCorrectly=False)),
#     }
#     test_distribution = {
#         "ACT_Distro": len(questions.filter(test_type='ACT')),
#         "SAT_Distro": len(questions.filter(test_type='SAT')),
#         "GRE_Distro": len(questions.filter(test_type='GRE')),
#     }
#     subject_distribution = {
#         "Math_Distro": len(questions.filter(subject="Math")),
#         "Reading_Distro": len(questions.filter(subject="Reading")),
#         "Science_Distro": len(questions.filter(subject="Science"))
#     }

#     context = {
#         'questions': questions[:3],
#         'all_tests': ['ACT', 'SAT', 'GRE'],
#         'test_type': str(test_type),
#         'accuracy': accuracy,
#         'test_distribution': test_distribution,
#         'subject_distribution': subject_distribution,
#     }

#     return render(request, 'users/profile_question_history.html', context)




@login_required
def profileUpdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, f'Your account has been updated')
        return redirect('profile', test_type='ALL')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/update_profile.html', context)




@login_required
def fullQuestionHistory(request, test_type):
    userProfile = Profile.objects.filter(user=request.user).first()
    if test_type == 'ALL':
        questions = userProfile.questions_answered.all().order_by("copyId")
    else:
        questions = userProfile.questions_answered.filter(test_type=test_type).order_by("copyId")
    context = {
        'questions': questions,
        'test_type': test_type,
    }

    return render(request, 'users/full_question_history.html', context)