from django.shortcuts import render

import yfinance as yf
import datetime

from django.http import JsonResponse

# Create your views here.


def perdelta(start, end, delta):
    curr = start

    while curr < end:
        yield curr
        curr += delta


def sensex_graph(request):
    diff = 1
    now = datetime.datetime.now().date()
    bef = now - datetime.timedelta(days=diff)
    print(now)

    data_min = yf.download("^BSESN", start=str(bef),
                           end=str(now), interval='1m')  # Getting Sensex Data per Minute
    min_x = []

    min_x_lbl = []

    for i in range(len(data_min)):
        min_x.append(data_min['Open'][i])

    for i in perdelta(datetime.datetime.now() - datetime.timedelta(days=diff), datetime.datetime.now(), datetime.timedelta(minutes=1)):
        if (len(min_x) > len(min_x_lbl)):
            min_x_lbl.append(str(i.strftime("%H:%M")))
        else:
            break
    data = {
        'min_x': min_x,
        'min_x_lbl': min_x_lbl,
    }
    return JsonResponse(data)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
