from django.shortcuts import render, redirect

import yfinance as yf
import datetime

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from accounts.models import UserInfo
from expenses.models import ExpenseData
from django.contrib.auth.models import User

# chatbot import
from chatbot.chatbotEngine import chatbot

# Create your views here.

def chatbot_request(request):
    user_response = request.GET.get("user_response")
    data = {
        "bot_response": chatbot(user_response)[0],
        "url": chatbot(user_response)[1]
    }
    return JsonResponse(data)

def perdelta(start, end, delta):
    curr = start

    while curr < end:
        yield curr
        curr += delta


@login_required
def sensex_graph(request):

    diff = request.GET.get('diff', None)
    inter = request.GET.get('interval', None)
    if diff is None:
        diff = 0
    else:
        diff = int(diff)
    if inter is None:
        inter = "1m"

    now = datetime.datetime.now().date()
    bef = now - datetime.timedelta(days=diff)

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

    diff = request.GET.get('diff', None)
    inter = request.GET.get('interval', None)
    if diff is None:
        diff = 0
    else:
        diff = int(diff)

    if inter is None:
        inter = "1m"

    now = datetime.datetime.now().date()
    bef = now - datetime.timedelta(days=diff)

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
    if str(request.user) == 'AnonymousUser':
        return render(request, 'index.html')
    else:
        try:
            expended_amt_q = ExpenseData.objects.values_list(
                'expense_amount', flat=True).filter(user=request.user)
            expended_amt = 0
            for i in range(0, len(expended_amt_q)):
                expended_amt = expended_amt + expended_amt_q[i]
        except ExpenseData.DoesNotExist:
            expended_amt = 0
        try:
            context = {
                'income': UserInfo.objects.values_list('income', flat=True).get(user=request.user),
                'expended_amt': expended_amt
            }
            return render(request, 'index.html', context)
        except UserInfo.DoesNotExist:
            return redirect("user_info_form")

# Not found and Server Error Pages


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
