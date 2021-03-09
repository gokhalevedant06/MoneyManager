from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('new/', views.new),
    path('user_info/', views.user_info),
    path('about/', views.about),
    path('schemes/', views.schemes),
    path('fd/', views.fd),
    path('rd/', views.rd),
    path('ppf/', views.ppf),
    path('mis/', views.mis),
    path('nsc/', views.nsc),
]
