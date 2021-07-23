from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http import JsonResponse

import pywhatkit as kit
import datetime


# Create your views here.


@api_view(['GET', 'POST'])
def send_message(request):
    if request.method == 'POST':

        name = request.data['nameOfStudent']
        course_enquired = request.data['courseEnquired']
        phone_number = request.data['phoneNumber']

        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute + 2

        # print(name, course_enquired, phone_number)
        message = f'Hello {name}, thnx for enquiring for {course_enquired}'

        kit.sendwhatmsg(phone_no=phone_number, message=message,
                        tab_close=True, wait_time=5, time_hour=hour, time_min=min, print_wait_time=True)

        return JsonResponse({
            "Completed": True
        })
    else:
        return JsonResponse({
            "Completed": False
        })
