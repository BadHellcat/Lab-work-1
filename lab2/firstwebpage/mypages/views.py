from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def hello(request):
    return HttpResponse(u'Привет, Мир!')

def static_handler(request):
    return render(request, 'static_handler.html')