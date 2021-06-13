from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import auth, User

from django.contrib import messages

from .models import Choice, UserInfo


from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from django.http import JsonResponse

from django.contrib.auth.decorators import user_passes_test, login_required

from django.core.mail import EmailMessage
from MoneyManager.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

from django.http import HttpResponseServerError
import socket
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

        subject = 'Welcome to Team Money Manager!'
        html_message = render_to_string('edm.html')
        msg = EmailMessage(subject, html_message,
                           EMAIL_HOST_USER, [request.POST.get('email')])
        msg.content_subtype = "html"
        try:
            msg.send()
        except socket.gaierror:
            return HttpResponseServerError()

        return redirect('user_info_form')
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


@login_required
def user_info_ajax(request):
    if request.method == "POST":
        value = request.POST.get('value')
        elem_id = request.POST.get('id')
        success = False
        qs = UserInfo.objects.get(user=request.user)

        if elem_id == "name":
            User.objects.filter(id=request.user.id).update(
                username=value 
            )
            success = True
        elif elem_id == "email":
            User.objects.filter(id=request.user.id).update(
                email=value
            )
            success = True
        elif elem_id == "income":
            qs.income = value
            success = True
        elif elem_id == "profession":
            qs.profession = value
            success = True
        else:
            success = False
        qs.save()

        data = {
            'success': success
        }
        return JsonResponse(data)
    else:
        choices = Choice.objects.all()

        serialized_choices = serialize(
            'json', choices, cls=DjangoJSONEncoder)

        return JsonResponse(serialized_choices, safe=False)


@login_required
def user_info_form(request):
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

        uinfo = UserInfo.objects.update_or_create(
            user=request.user,
            income=income,
            gender=gen,
            profession=prf
        )

        return redirect('user_info')
    else:
        if UserInfo.objects.filter(user=request.user).exists():
            return redirect('user_info')
        else:
            return render(request, "user_info_form.html")


@login_required
def user_info(request):
    context = {
        'data': UserInfo.objects.filter(user=request.user)
    }
    return render(request, 'user_info.html', context)
