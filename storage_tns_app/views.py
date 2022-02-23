from argparse import Action
from asyncio.windows_events import NULL
from typing import Type
from django.shortcuts import redirect, render
from .models import user,history,equipment,material

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
    material_item = material.objects.all()
    return render(request, 'show_material.html',{'material':material_item})


def show_equipment(request):
    equipment_item = equipment.objects.all()
    return render(request, 'show_equipment.html',{'equipment':equipment_item})

def addlist(request):
    if request.method == 'POST':
        #ตัวแปร สำหรับบันทึกค่า
        equipment_name = request.POST.get('name')
        type = request.POST.get('type')
        amount = request.POST.get('amount')
        picture = request.FILES
        #บันทึกเข้าที่ DB.equipment
        if type == 'equipment':
            equipment(Equipment=equipment_name,Amount=amount,Picture = picture).save()
        elif type == 'material':
            material(Material=equipment_name,Amount=amount,Picture = picture).save()
        #บันทึกเข้าที่ DB.history
        history(Equipment=equipment_name,Type=type,Action='ADD',Amount=amount).save()

    return render(request, 'addlist.html')

def delete(request):
    return render(request, 'delete.html')

def edit(request):
    return render(request, 'edit.html')

def edit_detail(request):
    return render(request, 'edit_detail.html')

def test(request):
    return render(request, 'test.html')


##def createLog(Equipment,Action,Amount):
 ##   if Equipment != '' and Action !='' and Amount != '':
  ##      history = history(Equipment=Equipment,Action=Action,Amount=Amount).save()
  ##      return 'OK'
 ##   else:
   ##     return 'Not ok'
# Create your views here.
