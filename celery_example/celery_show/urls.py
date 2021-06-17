
#from celery_example.celery_show.views import index
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index, name="index"),
]