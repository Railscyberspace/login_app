from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): 
    return HttpResponse("Hello You are on the Main app")