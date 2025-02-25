from . import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import profile


class usercreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class authentication(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class profilecreation(forms.ModelForm):
    class Meta:
        model = profile
        fields= ['userid','fname','lname','bio','location','working']