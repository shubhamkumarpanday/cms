from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib import auth, messages
from django.contrib.auth.models import Group
from django.urls import reverse

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("entered custom authentication")
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

# Create your views here.
def register(request):
    if (request.method == "POST"):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        email_address = request.POST["email_address"]
        password1 = request.POST["password"]
        password2 = request.POST["confirm_password"]
        print(first_name, last_name, user_name, email_address)
        print("password is", password1)
        print("confirm password is ", password2)
        if password1 == password2: 
                if User.objects.filter(email=email_address).exists():
                    messages.info(request, 'Username Taken')
                    print('UserName Taken');
                    return redirect('register')
                elif User.objects.filter(email=email_address).exists():
                    messages.info(request, "Email Taken")
                    print('Email Taken')
                    return redirect("register") 
                user = User.objects.create_user(username=user_name, password=password1, email=email_address,first_name=first_name, last_name=last_name)
                user.save();
                group = Group.objects.get(name="student")
                print("group is ", group);
                user.groups.add(group);
                print("User Created")
                return redirect("login")
        else: 
            print("Password aren't matching");
        return render(request, "register2.html")
    else:    
        return render(request, "register2.html")

    return render(request, "register2.html")

def login(request):
    if (request.method == "POST"):
        print(request)
        print("some morevalue")
        for key in request.POST:
            print(key , request.POST[key]);
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password, request.POST["type"])

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            request.session["type"] = request.POST["type"]
            return redirect("dashboard")
        
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
            
    return render(request, "login2.html")

def logout(request):
    del request.session["type"]
    auth.logout(request)
    return redirect("login")

def sample(request):
    return redirect("login")

def dashboard(request):
    return render(request, "dashboard3.html");