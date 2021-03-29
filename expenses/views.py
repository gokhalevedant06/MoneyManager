from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return render(request, 'expenses_index.html')


@login_required
def form(request):
    return render(request, 'expenses_form.html')
