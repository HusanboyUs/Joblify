from dataclasses import field
from django import forms
from .models import Jobs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserResgistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1']