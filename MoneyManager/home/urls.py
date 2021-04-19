from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
<<<<<<< HEAD
    path('about-us/', views.about, name="about"),
<<<<<<< HEAD
=======
    path('sensex-graph/', views.sensex_graph, name="sensex_graph"),
    path('nifty-graph/', views.nifty_graph, name="nifty_graph"),
>>>>>>> 9bc9982... added investment utility
=======

>>>>>>> 792a862... origin error solving 1
]
