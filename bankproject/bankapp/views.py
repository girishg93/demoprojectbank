from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from . models import Register


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        username=request.POST['usrnme']
        password=request.POST['pswd']
        confirm_password=request.POST['pswd1']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist. Please try another name")

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password and Confirm Password must be same")



    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['usrnme']
        password=request.POST['pswd']
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('buttonpage')
        else:
            messages.info(request,"Username or Password not matched")

    return render(request,'login.html')

def buttonpage(request):
    return render(request,'buttonpage.html')

def accountopening(request):
    return render(request,'accountopening.html')

def document(request):
    return render(request,'document.html')

def trivandram(request):
    return render(request,'trivandram.html')

def kollam(request):
    return render(request,'kollam.html')

def pathanamthitta(request):
    return render(request,'pathanamthitta.html')

def eranakulam(request):
    return render(request,'eranakulam.html')

def palakkad(request):
    return render(request,'palakkad.html')

def logout(request):
    auth.logout(request)
    return redirect('home')



