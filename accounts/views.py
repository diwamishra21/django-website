from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.



def login(request):
    if request.method == "POST":
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')




def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        username = request.POST['username']
        if password == c_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
                # for printing on console
                # print('Username taken')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
                #print('Email taken')
            else:
                user =  User.objects.create_user(username = username, password = c_password, email=email, first_name = first_name, last_name= last_name)
                user.save()
                messages.info(request,'User created Successfully')
                return redirect('login')
                #print("user created")
        else:
            messages.info(request,'Confirm Password should be same as password')
            return redirect('register')
            #print("Password is not same")
    else:
        return render(request,'accounts/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')