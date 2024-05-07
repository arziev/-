from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name='login'),
    path("register", views.register, name='register'),
    path("main", views.main, name='main'),
]