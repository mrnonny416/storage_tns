from django.shortcuts import render
from django.contrib import admin

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, admin.site.urls)

def login(request):
    return render(request, 'login.html')

def select(request):
    return render(request, 'select.html')
# Create your views here.
