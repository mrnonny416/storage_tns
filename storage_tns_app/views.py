from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def select(request):
    return render(request, 'select.html')

def show_material(request):
    return render(request, 'show_material.html')
# Create your views here.
