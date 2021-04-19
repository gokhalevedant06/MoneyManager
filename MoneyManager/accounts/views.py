from django.shortcuts import render, redirect
from django.http import JsonResponse
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
    if request.method == 'POST':
        if request.is_ajax():

            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()
        return redirect('/')
    else:
        if request.is_ajax():
            username = request.GET.get('username')
            email = request.GET.get('email')

            username_exists = False
            email_exists = False

            if User.objects.filter(username=username).exists():
                username_exists = True

            if User.objects.filter(email=email).exists():
                email_exists = True

            data = {
                'username_exists': username_exists,
                'email_exists': email_exists,
            }
            return JsonResponse(data)
        return render(request, 'register.html')
