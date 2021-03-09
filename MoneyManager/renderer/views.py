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


def about(request):
    return render(request, "about.html")

def schemes(request):
    return render(request, 'schemes.html')
    
def fd(request):
    return render(request, 'fd.html')

def rd(request):
    return render(request, 'rd.html')

def ppf(request):
    return render(request, 'ppf.html')

def mis(request):
    return render(request, 'mis.html')

def nsc(request):
    return render(request, 'nsc.html')