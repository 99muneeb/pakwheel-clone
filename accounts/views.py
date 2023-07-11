from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def LoginPage(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logined in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid login Credentils')
            return redirect('login')
    return render(request,'accounts/login.html')
def RegisterPage(request):
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already Exists:')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already Exists:')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    auth.login(request,user)
                    messages.success(request,'You are now logged in')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,'You are registeres successfuly')
                    return redirect('login')



        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
def LogoutPage(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'You are new successfully out')
        return redirect('home')

    return redirect('home')
def DashboardPage(request):
    return render(request,'accounts/dashboard.html')
