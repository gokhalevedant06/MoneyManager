from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
<<<<<<< HEAD
    path('test/', views.test),
=======
    path('new/',views.new),
    path('user_info/', views.user_info)
>>>>>>> ab874b579865adebd959ecfbb7ff195457068ae3
]
