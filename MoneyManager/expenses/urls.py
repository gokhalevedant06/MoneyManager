from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="exp_index"),
    path('fill-out-expenses/', views.form, name="exp_form"),
    path('expenses-form-ajax/', views.form_ajax, name="exp_form_ajax"),
]
