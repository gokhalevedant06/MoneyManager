from django.shortcuts import render, redirect

import datetime
import os

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from accounts.models import UserInfo
from expenses.models import ExpenseData
from django.contrib.auth.models import User


# Create your views here.


# def chatbot_request(request):

#     # chatbot import
#     from chatbot.chatbotEngine import chatbot

#     user_response = request.GET.get("user_response")
#     data = {
#         "bot_response": chatbot(user_response)[0],
#         "url": chatbot(user_response)[1]
#     }
#     return JsonResponse(data)

def index(request):
    if str(request.user) == 'AnonymousUser':
        return render(request, 'index.html')
    else:
        try:
            expended_amt_q = ExpenseData.objects.values_list(
                'expense_amount', flat=True).filter(user=request.user)
            expended_amt = 0
            for i in range(0, len(expended_amt_q)):
                expended_amt = expended_amt + expended_amt_q[i]
        except ExpenseData.DoesNotExist:
            expended_amt = 0
        try:
            context = {
                'income': UserInfo.objects.values_list('income', flat=True).get(user=request.user),
                'expended_amt': expended_amt
            }
            return render(request, 'index.html', context)
        except UserInfo.DoesNotExist:
            return redirect("user_info_form")

# Not found and Server Error Pages


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
