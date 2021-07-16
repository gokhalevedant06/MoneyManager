from django.shortcuts import render

from . import chatbotEngine
from rest_framework.decorators import api_view

from rest_framework.response import Response


@api_view(['GET', 'POST'])
def chatbotAPI(request):
    if request.method == 'POST':
        return Response({
            "bot_response": chatbotEngine.chatbot(request.data["user_response"])[0],
            "url": chatbotEngine.chatbot(request.data["user_response"])[1]
        })
    return Response({
        "bot_response": "SERVER_ERROR",
        "url": None,
    })
