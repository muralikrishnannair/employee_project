from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def myfunction(request):
    return HttpResponse("Welcome to Employee Project...!")

