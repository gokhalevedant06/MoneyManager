from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="exp_index"),
    path('fill-out-expenses', views.form, name="exp_form"),
]
