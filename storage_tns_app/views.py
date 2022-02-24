from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from .models import user,history,equipment,material


def login(request):
    isLogin = ''
    request.session['user'] = None#reset session('user')=NULL
    if request.method == 'POST':
        User = user.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        for eachUser in User:  
            if username != '' and password !='' and username == eachUser.Username and password and eachUser.Password == password:#Login Success
                request.session['user'] = username #{'user':'night'}
                return redirect('select')
    if request.POST.get('username'):
        isLogin = 'TRUE'
    return render(request, 'login.html',{'isLogin':isLogin})

def select(request):
    user = request.session.get('user')#user <- session  : user<-night
    if(user == None):#if not user 
        return redirect('login')#return to login.html
    return render(request, 'select.html',{'user':user})

def show_material(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    material_item = material.objects.all()
    return render(request, 'show_material.html',{'material':material_item,'user':user})

def show_equipment(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    equipment_item = equipment.objects.all()
    return render(request, 'show_equipment.html',{'equipment':equipment_item})

def addlist(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'POST':
        #ตัวแปร สำหรับบันทึกค่า
        equipment_name = request.POST.get('name')
        type = request.POST.get('type')
        amount = request.POST.get('amount')
        picture = request.FILES['customFile']
        #บันทึกเข้าที่ DB.equipment
        if type == 'equipment':
            equipment(Equipment=equipment_name,Amount=amount,Picture = picture).save()
            return redirect('show_equipment')
        elif type == 'material':
            material(Material=equipment_name,Amount=amount,Picture = picture).save()
            return redirect('show_material')
        #บันทึกเข้าที่ DB.history
        history(Equipment=equipment_name,Type=type,Action='ADD',Amount=amount).save()

    return render(request, 'addlist.html',{'user':user})

def delete_material(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    items = material.objects.all()
    if request.method == 'GET':
        if request.GET.get('id'):
            material.objects.filter(order=request.GET.get('id')).delete()
            return redirect('delete_material')
    return render(request, 'delete_material.html',{'items':items})

def delete_equipment(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    items = equipment.objects.all()
    if request.method == 'GET':
        if request.GET.get('id'):
            equipment.objects.filter(order=request.GET.get('id')).delete()
            return redirect('delete_equipment')
    return render(request, 'delete_equipment.html',{'items':items})

def edit_equipment(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    items = equipment.objects.all()
    return render(request, 'edit_equipment.html',{'items':items})

def edit_equipment_detail(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    if request.method == 'GET':
        equipment_id = request.GET.get('id')
        item = equipment.objects.filter(order=(equipment_id))
    return render(request, 'edit_equipment_detail.html',{'items':item})

def edit_material(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    items = material.objects.all()
    return render(request, 'edit_material.html',{'items':items})

def edit_material_detail(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    return render(request, 'edit_material_detail.html')

def test(request):
    
    return render(request, 'test.html')

def edit_equipment_save(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        equipment_name = request.POST.get('name')
        amount = request.POST.get('amount')
        if request.FILES:
            picture = request.FILES['customFile']
            equipment.objects.filter(order=request.GET.get('id')).delete()
            equipment(Equipment=equipment_name,Amount=amount,Picture = picture).save()
        else:
            equipment.objects.filter(order=id).update(Equipment=equipment_name,Amount=amount)
    return redirect('edit_equipment')