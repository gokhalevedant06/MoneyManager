from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('options/', TemplateView.as_view(template_name="schemes.html"),
         name="invest_index"),

    path('fixed-deposit/', TemplateView.as_view(template_name="fd.html"),
         name="fixed_deposit"),
    path('reccuring-deposit/', TemplateView.as_view(template_name="rd.html"),
         name="recurring_deposit"),
    path('public-provident-fund/',
         TemplateView.as_view(template_name="ppf.html"), name="provident_fund"),
    path('monthly-income-scheme/',
         TemplateView.as_view(template_name="mis.html"), name="monthly_income"),
    path('national-savings-certificate/', TemplateView.as_view(template_name="nsc.html"),
         name="national_savings_certificate"),
    path('crypto/', TemplateView.as_view(template_name="crypto.html"), name="crypto"),
    path('stock/', TemplateView.as_view(template_name="stock.html"), name="stock"),
    path('real-estate/', TemplateView.as_view(template_name="real.html"), name="real"),
    path('insurance/', TemplateView.as_view(template_name="insurance.html"),
         name="insurance"),

    path('form/', views.investment_form, name="investment_form"),
    path('form-ajax/', views.investment_form_ajax, name="investment_form_ajax"),
    path('form-ajax-interest/', views.investment_form_interest_rates,
         name="investment_form_ajax_interest"),
    path('previous-data/', views.investment_tbl, name="investment_tbl"),
    path('investment-tbl-ajax/', views.investment_tbl_ajax,
         name="investment_tbl_ajax"),

]
