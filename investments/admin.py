from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Schemes)
class SchemesAdmin(admin.ModelAdmin):
    list_display = [
        'bank_name',
        'scheme',
    ]

    list_filter = [
        'bank_name',
        'scheme',
    ]


@admin.register(SchemeRates)
class SchemeRatesAdmin(admin.ModelAdmin):
    list_display = [
        'scheme_name',
        'intrest_rate',
        'time_span',
    ]
    list_filter = [
        'intrest_rate',
        'time_span',
    ]
