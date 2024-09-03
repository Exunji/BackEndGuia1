from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola desde app de gabriel</h1>")

def segundaVista(request):
    return HttpResponse('<img src="https://ih1.redbubble.net/image.5020361835.3314/flat,750x,075,f-pad,750x1000,f8f8f8.jpg" alt="alternatetext">')