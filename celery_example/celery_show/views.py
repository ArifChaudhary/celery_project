from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
from django.core.mail import send_mail

from .helper import *



def index(request):
    #sleepy.delay(10)
    #send_mail_without_celery()
    send_email_task.delay()
    return HttpResponse("<h1>Hello, From CELERY</h1>")