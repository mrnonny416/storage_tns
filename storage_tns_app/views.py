
from django.shortcuts import redirect, render
from .models import user, history, storage, brand as brandDB

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
                return redirect('main')
    if request.POST.get('username'):
        isLogin = 'TRUE'
    return render(request, 'login.html', {'isLogin': isLogin})

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
    return render(request, 'main.html',{'user':user,'storage':items,'searchBox':searchBox})

def add_storage(request):
    user = request.session.get('user')
    Brand = brandDB.objects.all()
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
        storage_add = reversed(storage.objects.all())
        for item in storage_add:
            Name_order = item.order
            break
        history(Name_order=Name_order,Name=name, Brand=brand, Type=type,Action='ADD', Category=category, Amount=amount,Username=user).save()
    return render(request, 'add_storage.html', {'user': user,'Brand':Brand})

def test(request):
    items = storage.objects.all()
    return render(request, 'test.html',{'storage':items})

def product(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    Success = None
    if request.method == 'GET': #from Main
        items = storage.objects.filter(order=request.GET.get('id'))
        transaction = reversed(history.objects.filter(Name_order=request.GET.get('id')))
    if request.method == 'POST': #from product Action Borrow/Return
        items = storage.objects.filter(order=request.POST.get('id'))
        Success = action(user,request.POST.get('id'),request.POST.get('submit'),request.POST.get('quantity'))
        transaction = reversed(history.objects.filter(Name_order=request.POST.get('id')))
    return render(request, 'product.html',{'storage':items,'Success':Success,'transactions':transaction,'user':user})

def action(user,id,submit,quantity):
    items = storage.objects.filter(order=id)
    for item in items:
            if submit == 'borrow' and quantity != '0' and item.Amount >= int(quantity):
                if storage.objects.filter(order=id).update(Amount = item.Amount-int(quantity)):
                    history(Name_order=id,Name=item.Name, Brand=item.Brand, Type=item.Type,Action='Borrow', Category=item.Category, Amount=quantity,Username=user).save()
                    return 'True'
            elif submit == 'return' and quantity != '0':
                if storage.objects.filter(order=id).update(Amount = item.Amount+int(quantity)):
                    history(Name_order=id,Name=item.Name, Brand=item.Brand, Type=item.Type,Action='Return', Category=item.Category, Amount=quantity,Username=user).save()
                    return 'True'
    return 'False'
