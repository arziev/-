from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'time_management/login.html')

def register(request):
    # if request.method == 'POST':
        # name = request['name']
        # password = request['password']
        # password_check = request['password_check']
        # if password == password_check:
        #     User.objects.create_user(name=name, password=password)
        #     User.save()
        #     login(request, name)
        #     HttpResponseRedirect(reverse('index'))
        # else:
        #     return render(request, 'time_management/register', {"problem": "Пароли не совпадают. Повтортите попытку.."})
        
    # else:
    print(request)
    return render(request, 'time_management/register.html')
