from django.shortcuts import render
import random
from django.http import HttpResponseRedirect,HttpResponse
from contest.models import registration,social_contest
from django.contrib.auth import login,logout,authenticate
def newuser(request):
    res=render(request,'contest/register.html')
    return res
def saveuser(request):
    if request.method=='POST':
        data=request.POST
        users=registration()
        users.username=data['username']
        users.email=data['email']
        users.password=data['password']
        users.cnfpswd=data['cnfpswd']
        users.save()
    s="Your account has successfully created"
    return HttpResponse(s)
def user_login(request):
    user_info={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('http://localhost:8000/contest/home-page')
        else:
            user_info['error']="Your username or password is incorrect"
            return render(request,'contest/LoginPage.html',user_info)
    else:
        return render(request,'contest/LoginPage.html',user_info)
def home(request):
    res=render(request,'contest/homePage.html')
    return res
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/contest/LoginPage.html')
def contest(request):
    s=set()
    while(len(s)<10):
        s.add(random.randint(1,20))
    q=[]
    for index in s:
        q.append(social_contest.objects.all()[index])
    d={'q':q}
    res=render(request,'contest/contest.html',d)
    return res
def contest_result(request):
    question=10