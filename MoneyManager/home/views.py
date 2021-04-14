from django.shortcuts import render
# Create your views here.


<<<<<<< HEAD
=======
def perdelta(start, end, delta):
    curr = start

    while curr < end:
        yield curr
        curr += delta


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


>>>>>>> 176303e... debugging 16
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
