from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'field',
        'value'
    ]
    list_display_links = [
        'value'
    ]


admin.site.register(UserInfo)
