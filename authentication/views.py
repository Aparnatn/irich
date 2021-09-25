# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from authentication.models import mobile
from authentication.models import business_details
from authentication.forms import MobileLoginForm,BusinessForm
from .forms import business_detailsForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from authentication.models import transactions
from rest_framework import serializers
from serializers import TransactionsSerializer
from notifications.signals import notify


def index(request):
    try:
        users = User.objects.all()
        print(request.user)
        user = User.objects.get(username=request.user)
        return render(request, 'index.html', {'users': users, 'user': user})
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages from this view")


def message(request):
    try:
        if request.method == 'POST':
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(id=request.POST.get('user_id'))
            notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('index')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")

from django.core.files.storage import default_storage



def Home(request):
        if request.method == "POST":
            movie_form = business_detailsForm(request.POST)
            if movie_form.is_valid():
              movie_form.save()
              messages.success(request, ('Your movie was successfully added!'))
            else:
             messages.error(request, 'Error saving form')
             return redirect("home")
        movie_form = business_detailsForm()
        movies = business_details.objects.all()
        context={"movie_form":movie_form,"movie":movies}
        return render(request,"business.html",context)


def tablelist(request):
     movies = business_details.objects.all()
     context={"movie":movies}
     for i in movies:
       print(i.image1)

     return render(request,"tables.html",context)

