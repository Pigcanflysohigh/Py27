from django.shortcuts import render,redirect
from app01 import models
# Create your views here.

def login(request):
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('password')

        # if user == 'admin' and pwd == 'admin123.':
        #     return redirect('/index/')
        ret = models.User.objects.filter(name=user,password=pwd)
        if ret:
            return redirect('/index/')
        return render(request,'login.html',{'error':'用户/密码错误'})
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')