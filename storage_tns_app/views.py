
from django.shortcuts import redirect, render
from .models import user, history, storage, brand as brandDB,type as typeDB,category as categoryDB

def login(request):
    isLogin = ''
    if request.session.get('user') != None:
        return redirect('main')
    else:
        logout(request)
      # reset session('user')=NULL
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
    categorySearch = categoryDB.objects.all()
    typeSearch = typeDB.objects.all()
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        type = request.POST.get('type')
        category = request.POST.get('category')
        items = storage.objects.filter(Name__contains = keyword , Type__contains = type , Category__contains = category)
        return render(request, 'main.html',{'user':user,'storage':items,'keyword':keyword,'searchBox':searchBox ,'type':type,'category':category,'categorySearch':categorySearch,'typeSearch':typeSearch})
    else:
        items = reversed(storage.objects.all())
    return render(request, 'main.html',{'user':user,'storage':items,'searchBox':searchBox,'categorySearch':categorySearch,'typeSearch':typeSearch})

def add_storage(request):
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    Brand = brandDB.objects.all()
    Category = categoryDB.objects.all()
    Type = typeDB.objects.all()
    if request.method == 'POST' and request.FILES:
        if request.POST.get('submit') != 'OK':
            return redirect('main')
        # ตัวแปร สำหรับบันทึกค่า
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        type = request.POST.get('type')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        picture = request.FILES['customFile']
        masterkey = None
        # บันทึกเข้าที่ DB.
        storage_add = reversed(storage.objects.all())
        for item in storage_add:
            Name_order = item.order
            Name_order += 1
            break
        lastest_order = reversed(storage.objects.all())
        for item in lastest_order:
            if item.Type == type:
                masterkey = int((item.Masterkey)[3:])
                masterkey += 1
                break
        if masterkey == None:masterkey = 1
        for eachType in Type:
            if type == eachType.Type:
                masterkey = eachType.Prefix+str(masterkey)
        history(Name_order=Name_order,Masterkey=masterkey,Name=name, Brand=brand, Type=type,Action='ADD', Category=category, Amount=amount,Username=user).save()
        storage(Name=name,Masterkey=masterkey, Brand=brand, Type=type, Category=category, Amount=amount, Picture=picture).save()
        return redirect('main')
    return render(request, 'add_storage.html', {'user': user,'Brand':Brand,'Category':Category,'Type':Type})

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

def logout(request):
    request.session['user'] = None
    user = request.session.get('user')
    if(user == None):
        return redirect('login')
    return request