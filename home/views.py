from django.shortcuts import render

import yfinance as yf
import datetime

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from accounts.models import UserInfo
from expenses.models import ExpenseData
# Create your views here.


def perdelta(start, end, delta):
    curr = start

    while curr < end:
        yield curr
        curr += delta


@login_required
def sensex_graph(request):

    diff = int(request.GET.get('diff'))
    inter = request.GET.get('interval')

    now = datetime.datetime.now().date()
    bef = now - datetime.timedelta(days=diff)
    print(now)

    data_min = yf.download("^BSESN", start=str(bef),
                           end=str(now), interval=inter)  # Getting Sensex Data per Minute
    min_x = []

    min_x_lbl = []

    for i in range(len(data_min)):
        min_x.append(data_min['Open'][i])

    if inter == '1m':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(minutes=1)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%I:%M %p")))
            else:
                break
    elif inter == '30m':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(hours=1)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%I:%M %p")))
            else:
                break
    elif inter == '1wk':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(days=7)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%d %b %y")))
            else:
                break
    elif inter == '1mo':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(days=30)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%b %Y")))
            else:
                break
    data = {
        'min_x': min_x,
        'min_x_lbl': min_x_lbl,
    }
    return JsonResponse(data)


@login_required
def nifty_graph(request):

    diff = int(request.GET.get('diff'))
    inter = request.GET.get('interval')

    now = datetime.datetime.now().date()
    bef = now - datetime.timedelta(days=diff)
    print(now)

    data_min = yf.download("^NSEI", start=str(bef),
                           end=str(now), interval=inter)  # Getting Sensex Data per Minute
    min_x = []

    min_x_lbl = []

    for i in range(len(data_min)):
        min_x.append(data_min['Open'][i])

    if inter == '1m':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(minutes=1)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%I:%M %p")))
            else:
                break
    elif inter == '30m':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(hours=1)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%I:%M %p")))
            else:
                break
    elif inter == '1wk':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(days=7)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%d %b %y")))
            else:
                break
    elif inter == '1mo':
        for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(days=30)):
            if (len(min_x) > len(min_x_lbl)):
                min_x_lbl.append(str(i.strftime("%b %Y")))
            else:
                break
    data = {
        'min_x': min_x,
        'min_x_lbl': min_x_lbl,
    }
    return JsonResponse(data)


def index(request):
    try:
        expended_amt_q = ExpenseData.objects.values_list(
            'expense_amount', flat=True).filter(user=request.user)
        expended_amt = 0
        for i in range(0, len(expended_amt_q)):
            expended_amt = expended_amt + expended_amt_q[i]
    except ExpenseData.DoesNotExist:
        expended_amt = 0
    context = {
        'income': UserInfo.objects.values_list('income', flat=True).get(user=request.user),
        'expended_amt': expended_amt
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
