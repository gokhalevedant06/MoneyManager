from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from accounts.models import UserInfo
from .models import EXPENSES, ExpenseData

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

# Create your views here.


@login_required
def index(request):
    return render(request, 'expenses_index.html')


@login_required
def form(request):

    context = {
        'income': UserInfo.objects.values_list('income', flat=True).get(user=request.user),
        'data': ExpenseData.objects.filter(user=request.user)
    }
    return render(request, 'expenses_form.html', context)


@login_required
def form_ajax(request):
    if request.method == 'POST':
        expense_name = request.POST.get('expense_name')
        expense_amount = request.POST.get('expense_amount')
        remaining_amount = request.POST.get('remaining_amount')

        expense = ExpenseData(
            user=request.user,
            expense_name=expense_name,
            expense_amount=expense_amount,
            remaining_amount=remaining_amount
        )
        expense.save()

        UserInfo.objects.filter(user=request.user).update(
            income=remaining_amount)

        expenses = ExpenseData.objects.filter(user=request.user)

        expenseData = serialize('json', expenses, cls=DjangoJSONEncoder)

        data = {"data": expenseData}
        return JsonResponse(data)
    else:
        data = {
            'choice': EXPENSES,
        }
        return JsonResponse(data)
