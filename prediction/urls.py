from django.urls import path

from .views import sensex_prediction

urlpatterns = [
    path('', sensex_prediction, name='prediction'),
]

