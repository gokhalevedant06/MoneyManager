from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('new/', views.new),
    path('user_info/', views.user_info),
    path('about/', views.about,name="about"),
    path('schemes/', views.schemes,name="schemes"),
    path('fd/', views.fd,name="fd"),
    path('rd/', views.rd,name="rd"),
    path('ppf/', views.ppf,name="ppf"),
    path('mis/', views.mis,name="mis"),
    path('nsc/', views.nsc,name="nsc"),
]
