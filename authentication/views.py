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

@csrf_exempt
def transactionsApi(request,id=0):
    if request.method=='GET':
        transactions = Transactions.objects.all()
        transactions_serializer=TransactionsSerializer(transactions,many=True)
        return JsonResponse(transactions_serializer.data,safe=False)
    elif request.method=='POST':
        transactions_data=JSONParser().parse(request)
        transactions_serializer=TransactionsSerializer(data=transactions_data)
        if transactions_serializer.is_valid():
            transactions_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        transactions_data=JSONParser().parse(request)
        transactions=TransactionsSerializer.objects.get(transactionsId=transactions_data['transactionsId'])
        transactions_serializer=TransactionsSerializer(transactions,data=transactions_data)
        if transactions_serializer.is_valid():
            transactions_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        transactions=TransactionsSerializer.objects.get(transactionsId=id)
        transactions.delete()
        return JsonResponse("Deleted Successfully",safe=False)