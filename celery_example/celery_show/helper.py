from django.core.mail import send_mail
# Create your views here.

def send_mail_without_celery():
    send_mail("CELERY WORKED YEAH..!!", "CELERY IS NICE..!!", "uic.16mca8053@gmail.com", ["arif.chaudhary.geu864@gmail.com"], fail_silently=False)
    return None