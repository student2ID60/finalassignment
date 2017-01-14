from django import forms
from .models import Users

class UserForm(forms.Form):
    usernaam = forms.CharField()
    wachtwoord = forms.CharField()
    ingelogd = forms.BooleanField()