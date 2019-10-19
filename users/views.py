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
def profile(request):
    questions_answered = Profile.objects.filter(user=request.user).first().questions_answered.all().order_by("-id")

    context = {
        'questions_answered': questions_answered
    }

    return render(request, 'users/profile.html', context)



@login_required
def profileUpdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, f'Your account has been updated')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update_profile.html', context)
