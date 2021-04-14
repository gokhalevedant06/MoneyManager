from django.urls import path

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('sensex-graph/', views.sensex_graph, name="sensex_graph"),
    path('nifty-graph/', views.nifty_graph, name="nifty_graph"),
]
