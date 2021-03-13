from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.invest_index, name="invest_index"),

    path('fd/', views.fixed_deposit, name="fixed_deposit"),
    path('rd/', views.recurring_deposit, name="recurring_deposit"),
    path('ppf/', views.provident_fund, name="provident_fund"),
    path('mis/', views.monthly_income, name="monthly_income"),
    path('nsc/', views.national_savings_certificate,
         name="national_savings_certificate"),

    path('form/', views.investment_form, name="investment_form"),
    path('form-ajax/', views.investment_form_ajax, name="investment_form_ajax"),
    path('form-ajax-interest/', views.investment_form_interest_rates,
         name="investment_form_ajax_interest"),
]
