from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'time_management/index.html')

def gorilla(request):
    return render(request, 'time_management/gorilla.html')