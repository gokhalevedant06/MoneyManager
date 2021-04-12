from django.shortcuts import render
from .models import *

from pathlib import Path

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_info(request):
    if request.method == 'POST':
        pass
    else:
        if request.is_ajax():
            choices = Choice.objects.all()

            serialized_choices = serialize(
                'json', choices, cls=DjangoJSONEncoder)

            return JsonResponse(serialized_choices, safe=False)

        return render(request, "user_info.html")
