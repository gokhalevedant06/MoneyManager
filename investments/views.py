from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from accounts.models import UserInfo
from .models import InvestmentInfo, Schemes

from .models import BANK_NAMES, Schemes, SchemeRates

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

import math
import datetime

from django.db.models import Q
from django.template.loader import render_to_string
# Create your views here.


@login_required
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

    # ---------------------------------- FD Calculation ---------------------------------- #
    if '(FD)' in scheme:
        t1 = P * r * t
        t2 = t1/100
        A = P + t2
        is_fd = True
    else:
        is_fd = False

    # ---------------------------------- RD Calculation ---------------------------------- #
    if '(RD)' in scheme:
        t1 = 1 + r/400
        t2 = 4*t
        t3 = t1**t2
        A = math.floor(P*t3)
        is_rd = True
    else:
        is_rd = False

    # ---------------------------------- PPF Calculation ---------------------------------- #
    if '(PPF)' in scheme:
        t1 = r/100
        t2 = 1 + t1
        t3 = t2**t
        A = math.floor(P * t3)
        is_ppf = True
    else:
        is_ppf = False

    if '(NSC)' in scheme:
        t1 = P * (pow((1 + r / 100), 5))
        A = math.floor(t1)
        is_nsc = True
    else:
        is_nsc = False

    if '(MIS)' in scheme:
        t1 = r/100
        t2 = 1 + t1
        t3 = t2**t
        A = math.floor(P * t3)
        is_mis = True
    else:
        is_mis = False

    # Serializing rate objects into json format
    json_rate = serialize('json', rate, cls=DjangoJSONEncoder)
    data = {
        'rate': json_rate,
        'A': A,
        'is_fd': is_fd,
        'is_rd': is_rd,
        'is_ppf': is_ppf,
        'is_nsc': is_nsc,
        'is_mis': is_mis,
    }
    return JsonResponse(data)


@login_required
def investment_form_ajax(request):
    if request.method == 'POST':
        bank = request.POST.get('bank')
        time = request.POST.get('time')
        scheme = request.POST.get('scheme')
        principle = request.POST.get('principle')
        fd_time = request.POST.get('fd_time')
        intr_payout = request.POST.get('intr_payout')

        temp_date = datetime.datetime.now().date()
        maturity_date = temp_date.replace(year=temp_date.year + int(time))

        if scheme != '' and bank != '':
            scheme_id = Schemes.objects.filter(
                scheme__icontains=scheme).get(bank_name=bank)

            investment_info = InvestmentInfo(
                user=request.user,
                scheme_name=scheme_id,
                invested_amount=principle,
                timespan=time,
                intrest_payout=intr_payout,
                maturity_date=maturity_date,
            )

            print(investment_info)
            try:
                investment_info.save()
                updated_income = UserInfo.objects.values_list(
                    'income', flat=True).get(user=request.user) - int(principle)
                UserInfo.objects.filter(user=request.user).update(
                    income=updated_income)
                success = True
            except InvestmentInfo.DoesNotExist:
                success = False
        else:
            success = False

        data = {
            "success": success,
            "updated_income": updated_income
        }
    else:
        bank = request.GET.get('bank')

        scheme = Schemes.objects.filter(bank_name=bank)

        json_scheme = serialize('json', scheme, cls=DjangoJSONEncoder)

        data = {
            "schemes": json_scheme,
        }
    return JsonResponse(data)


@ login_required
def investment_form(request):
    if UserInfo.objects.filter(user=request.user).exists():
        salary = UserInfo.objects.values_list(
            'income', flat=True).get(user=request.user)
        context = {
            'salary': salary,
        }
        return render(request, 'investment_form.html', context)
    else:
        return redirect('user_info_form')


@login_required
def investment_tbl(request):
    context = {
        'data': InvestmentInfo.objects.filter(user=request.user)
    }
    return render(request, 'investment_tbl.html', context)


@login_required
def investment_tbl_ajax(request):
    query = request.GET.get('query', None)
    q = InvestmentInfo.objects.filter(user=request.user)
    if query is not None:
        queryset = q.filter(
            Q(scheme_name__scheme__icontains=query) |
            Q(scheme_name__bank_name__icontains=query) |
            Q(invested_amount__icontains=query) |
            Q(timespan__icontains=query) |
            Q(intrest_payout__icontains=query) |
            Q(maturity_date__icontains=query)
        )

    html = render_to_string(
        'investment_tbl_query.html',
        context={'data': queryset}
    )
    return JsonResponse({'html': html})
