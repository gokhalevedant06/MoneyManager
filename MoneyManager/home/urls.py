from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user-info', views.user_info, name="user_info")
]
