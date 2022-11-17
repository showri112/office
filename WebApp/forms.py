from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from .models import officemodel
from django import forms


class CreateForm(forms.ModelForm):
    Email = forms.EmailField()

    class Meta:
        model = officemodel
        fields = '__all__'



class UpdateForm(forms.ModelForm):
    class Meta:
        model = officemodel
        fields = '__all__'
        exclude = ['user']


class UserCreation(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
