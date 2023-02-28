import os

from celery import Celery, shared_task
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')

app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'Update_news_with_chatGPT': {
        'task': 'update_news',
        'schedule': crontab(hour=5)
    },
    'Update_db_and_mailing': {
        'task': 'update_news_mailing',
        'shedule': crontab(hour=6, minute=30)
    }
}
