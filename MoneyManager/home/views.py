from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

import yfinance as yf
import datetime

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
>>>>>>> 74066b0... added the expenses utility 01
# Create your views here.


<<<<<<< HEAD
=======
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


>>>>>>> 9bc9982... added investment utility
=======
from .models import *

from pathlib import Path

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from django.http import JsonResponse
=======
>>>>>>> fcb4e46... origin error solving 4
# Create your views here.


>>>>>>> 7efb37a... origin error solving 3
def index(request):
    return render(request, 'index.html')


<<<<<<< HEAD
<<<<<<< HEAD
def about(request):
    return render(request, 'about.html')
=======

from pathlib import Path
# Create your views here.


def index(request):
    return render(request, 'index.html')
>>>>>>> 792a862... origin error solving 1
=======
def user_info(request):
    if request.method == 'POST':
        pass
    else:
        if request.is_ajax():
            choices = Choice.objects.all()

            serialized_choices = serialize(
                'json', choices, cls=DjangoJSONEncoder)

            return JsonResponse(serialized_choices, safe=False)

        return render(request, "user_info.html")
>>>>>>> 7efb37a... origin error solving 3
=======
def about(request):
    return render(request, 'about.html')
>>>>>>> fcb4e46... origin error solving 4
