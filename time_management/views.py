from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.db import IntegrityError


from django.http import HttpResponseRedirect, JsonResponse
from .models import *
# Create your views here.

def main(request):
    # user = User()
    if request.method == "POST":
        print(request.POST.get('timer'))
        # print(request.POST.get('count'))

        # print(request.POST.get('stop'))
        return render(request, 'time_management/main.html', {"mes":"1000"})
    else:
        print(request.POST.get('count'))

        return render(request, 'time_management/main.html')
        

def logout_fun(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def login_fun(request):
    if request.method == 'POST':
        username = request.POST['name']
        print(request.POST['name'])
        password = request.POST['password']
        employee = authenticate(request, username=username, password=password)
        
        if employee != None:
            login(request, employee)
            return HttpResponseRedirect(reverse("main"))
        else:
            return render(request, 'time_management/login.html', {"problem":"Неправильный логин или пороль. Повторите попытку.."})
    else:
        return render(request, 'time_management/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        password_check = request.POST["password_check"]
        # email ="hello@gamil.com"
        if password == password_check:
            try:
                employee = User.objects.create_user(username, email, password)
                # user = User.objects.create_user(username, email, password)

                employee.save()
            except IntegrityError:
                print('hello')
                return render(request, 'time_management/register.html', {"problem": "Вы уже зарегистрироавны..."})

        # # Attempt to create new user
        # try:
        #     user = User.objects.create_user(username, email, password)
        #     user.save()
        # except IntegrityError:
        #     return render(request, "auctions/register.html", {
        #         "message": "Username already taken."
        #     })
        # login(request, user)
        # return HttpResponseRedirect(reverse("index"))
            login(request, employee)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'time_management/register.html', {"problem": "Пароли не совпадают. Повтортите попытку.."})
        
    # else:
    print(request)
    return render(request, 'time_management/register.html')