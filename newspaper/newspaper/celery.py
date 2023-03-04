import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')

app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.timezone = 'Asia/Baku'

# Periodical tasks, based in tasks.py.
app.conf.beat_schedule = {
    'Update_news_with_chatGPT': {
        'task': 'update_news',
        'schedule': crontab(minute=25, hour=12),
    },
    'Update_db_and_mailing': {
        'task': 'update_news_mailing',
        'schedule': crontab(minute=35, hour=12),
    }
}
