from django.db import models

class  base(models.Model):
    pass

class base_model(base):

    CreateBy = models.CharField(max_length=255, verbose_name='创建人', blank=True)
    CreateTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    UpdateBy = models.CharField(max_length=255, blank=True, verbose_name='更新人')
    UpdateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
