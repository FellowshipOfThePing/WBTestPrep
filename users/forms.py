from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegistrationForm(UserCreationForm):
    """Creates new User. 
    
    Requires Username and password. Email Optional
    """
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    """Updates Username and Email"""
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
    """Updates Profile Picture"""
    class Meta:
        model = Profile
        fields = ['image']