from django.contrib.auth.forms import UserCreationForm
from django import forms

from accountapp.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','company','phone_number','telecom', 'aws_access_key', 'aws_secret_key']
        widgets = {
            'aws_secret_key' : forms.PasswordInput(),
        }
