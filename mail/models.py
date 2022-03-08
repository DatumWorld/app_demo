from django.core.exceptions import ValidationError
from django.db import models

from common.base_model import base_model
from ckeditor.fields import RichTextField
# Create your models here.
class MailTaskTemplate(base_model):
    Name=models.CharField(max_length=255,verbose_name='模板名称',unique=True)
    Subject = models.CharField(max_length=255, verbose_name='主题')
    To=models.TextField(verbose_name='收件人')
    CC=models.TextField(verbose_name='抄送',blank=True)

    Content=RichTextField(blank=True,verbose_name='邮件正文')

    class Meta:
        managed = False
        db_table = 'MailTaskTemplate'
        verbose_name_plural  = '邮件任务模板'
        verbose_name = '邮件任务模板'

    def __str__(self):
        return self.Name

class MailTaskList(base_model):
    MailTaskTemplateId = models.ForeignKey(MailTaskTemplate,verbose_name='邮件任务模板名称',on_delete=models.CASCADE,db_column='MailTaskTemplateId')

    AddTime=models.DateTimeField(auto_now_add=True,verbose_name='添加时间',editable=False)
    Status=models.IntegerField(verbose_name='进度状态',editable=False,default=1,
                               choices=[(1,'等待中'),(2,'进行中'),(3,'已完成')])
    BeginTime = models.DateTimeField(verbose_name='开始时间', editable=False)
    FinishTime=models.DateTimeField(verbose_name='完成时间',editable=False)
    Success=models.IntegerField(verbose_name='是否成功',editable=False,
                               choices=[(1,'成功'),(2,'失败')])
    Log = models.TextField(verbose_name='日志',help_text='通常包含错误信息。', blank=True)

    class Meta:
        managed = False
        db_table = 'MailTaskList'
        verbose_name_plural  = '邮件任务'
        verbose_name='邮件任务'

    def __str__(self):
        return self.MailTaskTemplateId.Name