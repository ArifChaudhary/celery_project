from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    send_mail("CELERY WORKED YEAH..!!", "CELERY IS NICE..!!", "uic.16mca8053@gmail.com", ["arif.chaudhary.geu864@gmail.com"], fail_silently=False)
    print("MAIL FROM CELERY")
    return None