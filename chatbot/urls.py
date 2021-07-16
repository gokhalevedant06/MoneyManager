from django.urls import path

from .views import chatbotAPI
urlpatterns = [
    path('', chatbotAPI, name='chatbot_api'),
]
