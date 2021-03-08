from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index copy.html')


def login(request):
    return render(request, 'login.html')


def new(request):
    return render(request, 'new.html')


def user_info(request):
    return render(request, 'user_info.html')
