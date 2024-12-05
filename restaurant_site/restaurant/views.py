
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'all.html')

def contact(request):
    return  render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')



