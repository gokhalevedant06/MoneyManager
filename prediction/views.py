from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .timeseries import timeseries_prediction

import json
# Create your views here.


@api_view(['GET', 'POST'])
def sensex_prediction(request):
    if request.method == 'POST':
        print(request.data)
        try:
            ohlc = request.data['ohlc']
            nifty_or_bse = request.data['nifty_or_bse']
        except KeyError:
            return Response({
                "data": "Enter the right keys: ohlc, nifty_or_bse"
            })
        df = timeseries_prediction(30, nifty_or_bse, ohlc, 100)
        df['Date'] = df.index

        return Response(json.loads(df.to_json(orient='records', date_format='iso')))
    return Response({
        "data": "SERVER_ERROR"
    })
