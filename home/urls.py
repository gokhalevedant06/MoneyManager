# from chatbot.chatbotEngine import chatbot
from django.urls import path

from . import views

from django.views.generic import TemplateView

from .dash_apps import charts, prediction_charts

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('chatbot/', TemplateView.as_view(template_name="chatbot.html"), name='chatbot'),
    path('predictions/', TemplateView.as_view(template_name="predictions.html"),
         name='predictions')
]
