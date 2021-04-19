from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('about-us/', views.about, name="about"),
<<<<<<< HEAD
=======
    path('sensex-graph/', views.sensex_graph, name="sensex_graph"),
    path('nifty-graph/', views.nifty_graph, name="nifty_graph"),
<<<<<<< HEAD
>>>>>>> 9bc9982... added investment utility
=======

>>>>>>> 792a862... origin error solving 1
=======
    path('user-info', views.user_info, name="user_info")
>>>>>>> 7efb37a... origin error solving 3
=======
    path('about-us/', views.about, name="about"),
>>>>>>> fcb4e46... origin error solving 4
=======
>>>>>>> 176303e... debugging 16
>>>>>>> b89de65... origin error solving 5
]
