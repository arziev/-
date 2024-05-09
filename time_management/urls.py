from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_fun, name='login'),
    path("register", views.register, name='register'),
    path("main", views.main, name='main'),
    # path("timer", views.timer, name='timer'),
    path("logout", views.logout_fun, name='logout'),
]