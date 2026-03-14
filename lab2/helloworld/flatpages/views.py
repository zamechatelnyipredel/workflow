from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'static_handler.html', {})

def hello(request):
    return HttpResponse('Привет, Мир!')