import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')

app = Celery("management")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-1-minute': {
        'task': 'financial.tasks.add_to_db',
        'schedule': 60.0
    },
}