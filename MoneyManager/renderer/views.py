from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index copy.html')


def login(request):
    return render(request, 'login.html')


def test(request):
    return render(request, 'test.html')
