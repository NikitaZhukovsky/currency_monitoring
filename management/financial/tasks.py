from celery import shared_task
import time

from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings

@shared_task()
def add_to_db():
    time.sleep(5)
    return 'Aboba'


