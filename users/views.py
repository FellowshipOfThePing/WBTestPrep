from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile



def register(request):
    """Display Registration Page. Redirect to login after registration."""

    # If request is a post request, create a user with given info
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        # If the form is valid
        if form.is_valid():

            # Save form infom get the username data, and return a User Created message,
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')

            # redirect to the home page
            return redirect('login') 

    # If request is not a post request, fill in the form and redirect back to registration
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request, test_type):
    """Display Profile Page."""

    # Get profile instance for DB reference
    userProfile = request.user.profile
    userQuestions = userProfile.questions_answered


    # Default Iterables
    TEST_TYPES = ['ALL', 'SAT', 'ACT', 'GRE']
    SUBJECTS = ['Math', 'Reading', 'Science', 'English', 'Quantitative', 'Verbal']


    # Modify iterables based on test_type
    if test_type == 'ALL':
        questions = userQuestions.all()
    elif test_type == 'SAT':
        questions = userQuestions.filter(test_type=test_type).all()
        SUBJECTS = ['Math', 'Reading']
    elif test_type == 'ACT':
        questions = userQuestions.filter(test_type=test_type).all()
        SUBJECTS = ['Science', 'English']
    else:
        questions = userQuestions.filter(test_type=test_type).all()
        SUBJECTS = ['Quantitative', 'Verbal']


    # ------- Stats Filtered by Test ------- #


    # Truncate improvement line chart dates
    testImprovementDates = []
    for i in range(len(questions)):
        if i == 0 or i == len(questions) - 1:
            testImprovementDates.append(str(questions[i].date_answered)[5:10])
        else:
            testImprovementDates.append("")


    # Create improvement line chart list
    if test_type == 'ALL':
        testAccuracyList = [question.currentGeneralAccuracy for question in questions]
    else:
        testAccuracyList = [question.currentTestAccuracy for question in questions]


    # Dictionary for context
    by_test = {
        # Total Answer Accuracy (Pie Chart)
        'questionsCorrect': len(questions.filter(answeredCorrectly=True).all()),
        'questionsWrong': len(questions.filter(answeredCorrectly=False).all()),

        # Accuracy Over Time (Line Chart)
        'improvementDates': testImprovementDates,
        'improvementNodes': testAccuracyList
    }


    # Get question history and set order for list
    if test_type == 'ALL':
        questions = userQuestions.all().order_by("-copyId")
    else:
        questions = userQuestions.filter(test_type=test_type).all().order_by("-copyId")


    # Store profile for rendering in template
    context = {
        'questions': questions[:3],
        'by_test': by_test,
        'all_tests': TEST_TYPES,
        'test_type': test_type
    }

    return render(request, 'users/profile.html', context)



@login_required
def profileUpdate(request):
    """Display Profile Update Form"""

    # If request is a post request, update user/profile with given info, and redirect to profile view
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
    """Display extended Question History, filtered by test type."""

    # Get Profile Instance
    userProfile = request.user.profile

    # Get question history and set order
    if test_type == 'ALL':
        questions = userProfile.questions_answered.all().order_by("copyId")
    else:
        questions = userProfile.questions_answered.filter(test_type=test_type).order_by("copyId")

    # Store Question History Information for rendering in template
    context = {
        'questions': questions,
        'test_type': test_type,
    }

    return render(request, 'users/full_question_history.html', context)