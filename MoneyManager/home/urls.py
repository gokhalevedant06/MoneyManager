from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="about"),
    path('sensex-graph/', views.sensex_graph, name="sensex_graph"),
    path('nifty-graph/', views.nifty_graph, name="nifty_graph"),
]
