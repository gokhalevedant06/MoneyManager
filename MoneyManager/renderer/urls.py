from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('new/', views.new),
    path('user_info/', views.user_info)
]
