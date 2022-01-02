from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Dsuser

class LoginForm(forms.Form): 
    userId = forms.CharField()
    userPw = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Dsuser
        fields=[
            "userId"    ,
            "userPw"
        ]