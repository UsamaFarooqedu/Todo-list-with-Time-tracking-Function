# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import Task
import datetime

def soft_reminder_and_auto_delete():
    now = timezone.now()
    for task in Task.objects.all():
        if task.completion_time:
            if now + datetime.timedelta(minutes=5) >= task.completion_time and not task.completed:
                print(f"[Reminder] Task '{task.title}' is due in less than 5 minutes.")
            if now >= task.completion_time:
                print(f"[Auto Delete] Task '{task.title}' deleted at {now}")
                task.delete()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(soft_reminder_and_auto_delete, 'interval', minutes=1)
    scheduler.start()
