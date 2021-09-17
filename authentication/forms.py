# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from authentication.models import mobile
from authentication.models import business
from authentication.forms import mobile

class MobileLoginForm(forms.Form):
     phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "phone",
                "class": "form-control"
            }
        ))
class Meta:
        model = mobile
        fields = ('sId','phone',)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Firstname",
                "class": "form-control"
            }
        ))
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Lastname",
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",
                "class": "form-control"
            }
        ))
    customercode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "customer code",
                "class": "form-control"
            }
        ))
    communitycode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "community code",
                "class": "form-control"
            }
        ))
    salescode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "sales code",
                "class": "form-control"
            }
        ))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2','communitycode','customercode','mobile','lastname','salescode')


