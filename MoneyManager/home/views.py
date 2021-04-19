from django.shortcuts import render

from pathlib import Path
# Create your views here.


def index(request):
    return render(request, 'index.html')
