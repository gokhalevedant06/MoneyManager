from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User

# Create your views here.


def login(request):
    ''' Logs in  a user an authenticates him '''

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    ''' Logs out a user '''

    auth.logout(request)
    return redirect('/')


def register(request):
    ''' Registers a new user '''

    return render(request, 'register.html')
