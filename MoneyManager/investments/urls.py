from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.invest_index, name="invest_index"),

    path('fixed-deposit/', views.fixed_deposit, name="fixed_deposit"),
    path('reccuring-deposit/', views.recurring_deposit, name="recurring_deposit"),
    path('public-provident-fund/', views.provident_fund, name="provident_fund"),
    path('monthly-income-scheme/', views.monthly_income, name="monthly_income"),
    path('national-savings-certificate/', views.national_savings_certificate,
         name="national_savings_certificate"),
    path('crypto/', views.crypto, name="crypto"),
    path('stock/', views.stock, name="stock"),
    path('real-estate/', views.real, name="real"),
     path('insurance/', views.insurance, name="insurance"),

    path('form/', views.investment_form, name="investment_form"),
    path('form-ajax/', views.investment_form_ajax, name="investment_form_ajax"),
    path('form-ajax-interest/', views.investment_form_interest_rates,
         name="investment_form_ajax_interest"),
]
