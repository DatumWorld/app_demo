from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import shared_task

app=Celery()

# let celery workers take and do the work
@shared_task
def mail_task(ids):
    # mail code here
    try:
        # from common.mail import mail...
        pass
        return True
    except:
        return False