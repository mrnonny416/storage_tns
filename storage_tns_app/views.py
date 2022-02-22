from django.shortcuts import redirect, render
from .models import user 

def login(request):
    isLogin = ''
    username = ''
    password = ''
    if request.method == 'POST':     
        User = user.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        for eachUser in User:  
            if username != '' and password !='' and username == eachUser.Username and password and eachUser.Password == password:
                isLogin = 'True'
                return redirect('select')
            else:
                isLogin = 'False'
        if isLogin=='True':
            print('OK')
        elif isLogin=='False':
            print('not OK')       
    return render(request, 'login.html')


def select(request):
    return render(request, 'select.html')

def show_material(request):
    return render(request, 'show_material.html')


def show_equipment(request):
    return render(request, 'show_equipment.html')

def addlist(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
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
