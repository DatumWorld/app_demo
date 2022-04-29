from __future__ import absolute_import, unicode_literals

import datetime
import traceback

from celery import Celery
from celery import shared_task
from .models import MailTaskTemplate, MailTaskList
from common.mail import mail

app = Celery()


# let celery workers take and do the work
@shared_task
def mail_task(ids):
    i=0
    for id in ids:
        try:
            # mail code here
            qs = MailTaskList.objects.filter(id=id).first()
            mt_id = qs.MailTaskTemplateId_id
            mt = MailTaskTemplate.objects.filter(id=mt_id).first()
            result=mail(To=mt.To, CC=mt.CC, Content=mt.Content, Subject=mt.Subject)
            if result:
                i=i+1
        except:
            error = traceback.format_exc()
            print(f'''{datetime.datetime.now()}\n{id}\n{error}''',
                  file=open('/log/mailError.txt', mode='a', encoding='utf-8'))
            continue
    return i

