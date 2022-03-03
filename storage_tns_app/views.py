from asyncio.windows_events import NULL
import re
from django.shortcuts import redirect, render
from .models import user, history, equipment, material, storage

def login(request):
    isLogin = ''
    request.session['user'] = None  # reset session('user')=NULL
    if request.method == 'POST':
        User = user.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        for eachUser in User:
            if username != '' and password != '' and username == eachUser.Username and password and eachUser.Password == password:  # Login Success
                request.session['user'] = username  # {'user':'night'}
                return redirect('select')
    if request.POST.get('username'):
        isLogin = 'TRUE'
    return render(request, 'login.html', {'isLogin': isLogin})

def select(request):
    user = request.session.get('user')  # user <- session  : user<-night
    if(user == None):  # if not user
        return redirect('login')  # return to login.html
    return render(request, 'select.html', {'user': user})

def show_material(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        material_item = material.objects.filter(Material__contains=request.POST.get('keyword'))
    else:
        material_item = material.objects.all()
        if request.method == 'GET' and request.GET.get('action'):
            for items in material_item:
                if int(request.GET.get('id')) == items.order:
                    material.objects.filter(order=items.order).update(Amount=items.Amount+int(request.GET.get('action')))
                    if request.GET.get('action') == '1': history(Equipment=items, Type='Material',Action='Return', Amount=1,Username=user).save()
                    elif request.GET.get('action') == '-1': history(Equipment=items, Type='Material',Action='Borrow', Amount=1,Username=user).save()
                    return redirect('show_material')
    return render(request, 'show_material.html', {'material': material_item, 'user': user})

def main(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    searchBox = storage.objects.all()
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        items = storage.objects.filter(Name__contains = keyword)
        return render(request, 'main.html',{'user':user,'storage':items,'keyword':keyword,'searchBox':searchBox})
    else:
        items = storage.objects.all()
    print(searchBox)
    return render(request, 'main.html',{'user':user,'storage':items,'searchBox':searchBox})

def show_equipment(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        equipment_item = equipment.objects.filter(Equipment__contains=request.POST.get('keyword'))
    else:
        equipment_item = equipment.objects.all()
    if request.method == 'GET' and request.GET.get('action'):
        for items in equipment_item:
            if int(request.GET.get('id')) == items.order:
                equipment.objects.filter(order=items.order).update(Amount=items.Amount+int(request.GET.get('action')))
                if request.GET.get('action') == '1': history(Equipment=items, Type='Equipment',Action='Return', Amount=1,Username=user).save()
                elif request.GET.get('action') == '-1': history(Equipment=items, Type='Equipment',Action='Borrow', Amount=1,Username=user).save()
                return redirect('show_equipment')
    return render(request, 'show_equipment.html', {'equipment': equipment_item,'user':user})

def addlist(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        # ตัวแปร สำหรับบันทึกค่า
        equipment_name = request.POST.get('name')
        type = request.POST.get('type')
        amount = request.POST.get('amount')
        picture = request.FILES['customFile']
        # บันทึกเข้าที่ DB.equipment
        if type == 'equipment':
            equipment(Equipment=equipment_name,
                      Amount=amount, Picture=picture).save()
            history(Equipment=equipment_name, Type=type,Action='ADD', Amount=amount,Username=user).save()
            return redirect('show_equipment')
        elif type == 'material':
            material(Material=equipment_name,
                     Amount=amount, Picture=picture).save()
            history(Equipment=equipment_name, Type=type,Action='ADD', Amount=amount,Username=user).save()
            return redirect('show_material')
    return render(request, 'addlist.html', {'user': user})

def add_storage(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        # ตัวแปร สำหรับบันทึกค่า
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        type = request.POST.get('type')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        picture = request.FILES['customFile']
        # บันทึกเข้าที่ DB.
        storage(Name=name, Brand=brand, Type=type, Category=category, Amount=amount, Picture=picture).save()
        history(Name=name, Brand=brand, Type=type,Action='ADD', Category=category, Amount=amount,Username=user).save()
    return render(request, 'add_storage.html', {'user': user})

def edit_equipment(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        items = equipment.objects.filter(Equipment__contains=request.POST.get('keyword'))
    else:
        items = equipment.objects.all()
    return render(request, 'edit_equipment.html', {'items': items,'user':user})


def edit_equipment_detail(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'GET':
        equipment_id = request.GET.get('id')
        item = equipment.objects.filter(order=(equipment_id))
    return render(request, 'edit_equipment_detail.html', {'items': item,'user':user})


def edit_material(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        items = material.objects.filter(Material__contains=request.POST.get('keyword'))
    else:
        items = material.objects.all()
    return render(request, 'edit_material.html', {'items': items,'user':user})

def edit_material_detail(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'GET':
        material_id = request.GET.get('id')
        item = material.objects.filter(order=(material_id))
    return render(request, 'edit_material_detail.html', {'items': item,'user':user})

def edit_equipment_save(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        equipment_name = request.POST.get('name')
        amount = request.POST.get('amount')
        if request.FILES:
            picture = request.FILES['customFile']
            equipment.objects.filter(order=request.GET.get('id')).delete()
            equipment(Equipment=equipment_name,Amount=amount, Picture=picture).save()
        else:
            equipment.objects.filter(order=id).update(Equipment=equipment_name, Amount=amount)
        history(Equipment=equipment_name, Type='Equipment',Action='edit', Amount=amount,Username=user).save()
    return redirect('edit_equipment')

def edit_material_save(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        material_name = request.POST.get('name')
        amount = request.POST.get('amount')
        if request.FILES:
            picture = request.FILES['customFile']
            material.objects.filter(order=request.GET.get('id')).delete()
            material(Material=material_name,Amount=amount, Picture=picture).save()
        else:
            material.objects.filter(order=id).update(Material=material_name, Amount=amount)
        history(Equipment=material_name, Type='Equipment',Action='edit', Amount=amount,Username=user).save()
    return redirect('edit_material')

def test(request):
    items = storage.objects.all()
    return render(request, 'test.html',{'storage':items})

def delete_material(request):
    if request.method == 'GET' and request.GET.get('id'):
        material.objects.filter(order=request.GET.get('id')).delete()
    return redirect('edit_material')

def delete_equipment(request):
    if request.method == 'GET':
        if request.GET.get('id'):
            equipment.objects.filter(order=request.GET.get('id')).delete()
    return redirect('edit_equipment')

def product(request):
    if request.method == 'GET':
        items = storage.objects.filter(order=request.GET.get('id'))
    return render(request, 'product.html',{'storage':items})
