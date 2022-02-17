from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def select(request):
    return render(request, 'select.html')

def show_material(request):
    return render(request, 'show_material.html')


def show_equipment(request):
    return render(request, 'show_equipment.html')

def addlist(request):
    return render(request, 'addlist.html')

def delete(request):
    return render(request, 'delete.html')

def edit(request):
    return render(request, 'edit.html')

def edit_detail(request):
    return render(request, 'edit_detail.html')

def test(request):
    return render(request, 'test.html')
# Create your views here.
