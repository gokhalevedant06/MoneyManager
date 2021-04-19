from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import auth, User

from django.contrib import messages

from .models import *


from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from django.http import JsonResponse
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
            messages.warning(
                request, "Username or Password is incorrect!", fail_silently=False)
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


def user_info_ajax(request):
    if request.is_ajax():
        choices = Choice.objects.all()

        serialized_choices = serialize(
            'json', choices, cls=DjangoJSONEncoder)

        return JsonResponse(serialized_choices, safe=False)


def user_info(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')

        income = request.POST.get('income')
        gen = request.POST.get('gender')
        prf = request.POST.get('profession')

        User.objects.filter(id=request.user.id).update(
            first_name=fname,
            last_name=lname
        )

        uinfo = UserInfo(
            user=request.user,
            income=income,
            gender=gen,
            profession=prf
        )
        uinfo.save()

        return redirect('user_info')
    else:
        return render(request, "user_info.html")
