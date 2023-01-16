from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields= ['username', 'first_name', 'last_name', 'email','password1', 'password2']


class LoginForm(forms.Form):

    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)