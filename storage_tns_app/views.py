from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from .models import user,history,equipment,material


def login(request):
    isLogin = '' 
    if request.method == 'POST':
        User = user.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        for eachUser in User:  
            if username != '' and password !='' and username == eachUser.Username and password and eachUser.Password == password:
                request.session['user'] = username
                return redirect('select')
    if request.POST.get('username'):
        print(request.POST.get('username'))
        isLogin = 'TRUE'
    return render(request, 'login.html',{'isLogin':isLogin})


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

    return render(request, 'addlist.html')

def delete_material(request):
    items = material.objects.all()
    if request.method == 'GET':
        if request.GET.get('id'):
            material.objects.filter(order=request.GET.get('id')).delete()
            return redirect('delete_material')
    return render(request, 'delete_material.html',{'items':items})

def delete_equipment(request):
    items = equipment.objects.all()
    if request.method == 'GET':
        if request.GET.get('id'):
            equipment.objects.filter(order=request.GET.get('id')).delete()
            return redirect('delete_equipment')
    return render(request, 'delete_equipment.html',{'items':items})

def edit_equipment(request):
    equipment_item = equipment.objects.all()
    return render(request, 'edit_equipment.html',{'equipment':equipment_item})

def edit_equipment_detail(request):
    return render(request, 'edit_equipment_detail.html')

def edit_material(request):
    return render(request, 'edit_material.html')

def edit_material_detail(request):
    return render(request, 'edit_material_detail.html')

def test(request):
    return render(request, 'test.html')


##def createLog(Equipment,Action,Amount):
 ##   if Equipment != '' and Action !='' and Amount != '':
  ##      history = history(Equipment=Equipment,Action=Action,Amount=Amount).save()
  ##      return 'OK'
 ##   else:
   ##     return 'Not ok'
# Create your views here.
