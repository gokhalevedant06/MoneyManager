from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def sensex_prediction(request):
    if request.method == 'POST':
        return Response({
            "data": request.data
        })
    return Response({
        "data": "SERVER_ERROR"
    })