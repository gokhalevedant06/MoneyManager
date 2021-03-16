from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),

    path('user-info-form/', views.user_info_form, name="user_info_form"),
    path('user-info/', views.user_info, name="user_info"),

    path('user-info-ajax', views.user_info_ajax, name="user_info_ajax"),
]
