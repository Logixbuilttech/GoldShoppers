from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


# Create a UserUpdateForm to update a username and email
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = "__all__"

class UploadfileForms(forms.Form):
    file = forms.FileField()