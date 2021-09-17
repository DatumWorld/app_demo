from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import shared_task

app=Celery()

# let celery workers take and do the work
@shared_task
def share_task(username=None):
    # your code here
    try:
        pass
        return True
    except:
        return False