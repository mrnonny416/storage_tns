from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def select(request):
    return render(request, 'select.html')
# Create your views here.
