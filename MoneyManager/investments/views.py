from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from accounts.models import UserInfo

from .models import BANK_NAMES, Schemes, SchemeRates

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
# Create your views here.


def investment_form_interest_rates(request):
    bank = request.GET.get('bank')
    scheme = request.GET.get('scheme')
    time = request.GET.get('time')
    P = int(request.GET.get('principle'))
    t = int(request.GET.get('fd_time'))

    q = Schemes.objects.filter(bank_name=bank)

    scheme_id = q.values_list(
        'id', flat=True).get(scheme=scheme)

    rate = SchemeRates.objects.filter(
        scheme_name=scheme_id).filter(time_span=time)

    r = SchemeRates.objects.filter(time_span=time).values_list(
        'intrest_rate', flat=True).get(scheme_name=scheme_id)

    if '(FD)' in scheme:
        t1 = P * r * t
        t2 = t1/100
        A = P + t2

    json_rate = serialize('json', rate, cls=DjangoJSONEncoder)
    data = {
        'rate': json_rate,
        'A': A
    }
    return JsonResponse(data)


def investment_form_ajax(request):
    bank = request.GET.get('bank')

    scheme = Schemes.objects.filter(bank_name=bank)

    json_scheme = serialize('json', scheme, cls=DjangoJSONEncoder)

    data = {
        "schemes": json_scheme,
    }
    return JsonResponse(data)


@ login_required
def investment_form(request):
    salary = UserInfo.objects.values_list(
        'income', flat=True).get(user=request.user)
    context = {
        'salary': salary,
    }
    return render(request, 'investment_form.html', context)


def invest_index(request):
    return render(request, 'schemes.html')


def fixed_deposit(request):
    return render(request, 'fd.html')


def recurring_deposit(request):
    return render(request, 'rd.html')


def provident_fund(request):
    return render(request, 'ppf.html')


def monthly_income(request):
    return render(request, 'mis.html')


def national_savings_certificate(request):
    return render(request, 'nsc.html')
<<<<<<< HEAD

def crypto(request):
    return render(request, 'crypto.html')

def stock(request):
    return render(request, 'stock.html')
    
def real(request):
    return render(request, 'real.html')

def insurance(request):
    return render(request, 'insurance.html')


=======
>>>>>>> b89de65... origin error solving 5
