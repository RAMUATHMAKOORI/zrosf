from django.shortcuts import render,redirect
from .models import std
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    return render(request,'home.html')


def ad(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            if request.POST.get('year') and request.POST.get('name') and request.POST.get('tel'):
                s=std()
                s.name=request.POST.get('name')
                s.year=request.POST.get('year')
                s.phone=request.POST.get('tel')
                s.save()
                messages.info(request,'Data added')
                return redirect('add1')
                
    else:
        messages.info(request,'Please login')
        return redirect('login')
def res(request):
    if request.user.is_authenticated:
        return render(request,'res.html')
    else:
        messages.info(request,'please login')
        return redirect('login')
        
        
def res1(request):
    return render(request,'res1.html')
    
def dp(request):
    if request.method=='POST':
        if request.POST.get('year'):
            s1=request.POST.get('year')
            a= std.objects.filter(year=s1)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('res')
                
            else:
                return render(request,'dp.html',{'a':a,'s1':s1})

def dp1(request):
    if request.method=='POST':
        if request.POST.get('year'):
            s1=request.POST.get('year')
            a= std.objects.filter(year=s1)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('res1')
            else:
                return render(request,'dp1.html',{'a':a,'s1':s1})            
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')       

                    
def delete(request):
    if request.user.is_authenticated:
        return render(request,'delete.html')
    else:
        return render(request,'login.html')
def update(request):
    if request.user.is_authenticated:
        return render(request,'update.html')
    else:
        return render(request,'login.html')
def updat(request):
    if request.user.is_authenticated:
        return render(request,'updat.html')
    else:
        return render(request,'login.html')
    
def updt(request):
    if request.user.is_authenticated:
        return render(request,'updt.html')
    else:
        return render(request,'login.html')

def chnm(request):
    if request.method=='POST':
        if request.POST.get('year') and request.POST.get('tel') and request.POST.get('name'):
            s1=request.POST.get('year')
            tel=request.POST.get('tel')
            name=request.POST.get('name')
            a= std.objects.filter(year=s1).filter(phone=tel)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('update')
            else:
                std.objects.filter(year=s1).filter(phone=tel).update(name=name)
                messages.info(request,'Name updated')
                return redirect('update')

def chpn(request):
    if request.method=='POST':
        if request.POST.get('year') and request.POST.get('tel') and request.POST.get('name'):
            s1=request.POST.get('year')
            tel=request.POST.get('tel')
            name=request.POST.get('name')
            a= std.objects.filter(year=s1).filter(name=name)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('update')
            else:    
                std.objects.filter(year=s1).filter(name=name).update(phone=tel)
                messages.info(request,'Phone number updated')
                return redirect('update')
            
def delt(request):
    if request.method=='POST':
        if request.POST.get('year') and request.POST.get('tel'):
            s1=request.POST.get('year')
            tel=request.POST.get('tel')
            a= std.objects.filter(year=s1).filter(phone=tel)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('update')
            else:
                std.objects.filter(year=s1).filter(phone=tel).delete()
                messages.info(request,'Data Deleted')
                return redirect('update')