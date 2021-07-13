from chatbot.chatbotEngine import chatbot
from django.urls import path

from . import views

from django.views.generic import TemplateView

from .dash_apps import charts

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('chatbot-ajax/', views.chatbot_request, name="chatbot_ajax"),
    path('chatbot/', TemplateView.as_view(template_name="chatbot.html"), name='chatbot')
]
