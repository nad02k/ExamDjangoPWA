from celery import Celery
from celery.schedules import crontab

# Set default Django settings module
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pwa_project.settings')

app = Celery('pwa_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Add periodic tasks
app.conf.beat_schedule = {
    'precache-assets-every-1-hour': {
        'task': 'assets.tasks.precache_asset',
        'schedule': crontab(minute=0, hour='*'),
        'args': ('https://example.com/style.css ',)
    },
    'run-usage-analytics-daily': {
        'task': 'assets.tasks.analyze_usage',
        'schedule': crontab(minute=0, hour=0),
    }
}