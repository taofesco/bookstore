# accounts/forms.py
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email')

        help_texts = {
            'username': 'Make something unique',
            'email': None,
        }


class UserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email')
