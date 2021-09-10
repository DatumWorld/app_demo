from django.db import models
from ckeditor.fields import RichTextField
from mptt.models import TreeForeignKey, MPTTModel
# Create your models here.

# the following code is for demo only，it doesn't work
class Task(MPTTModel):
    name = models.CharField(verbose_name='任务节点名称', max_length=50)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='上级任务节点名称'
    )
    active = models.BooleanField(verbose_name='是否有效', default=1)
    order = models.IntegerField(verbose_name='顺序', default=0 )

    unifiedTask_id = models.ForeignKey(UnifiedTask, verbose_name='任务模板名称', blank=True, null=True,
                                       on_delete=models.CASCADE, db_column='unifiedTask_id',
                                       help_text='')

    description = RichTextField(blank=True, verbose_name='详细描述')

    class Meta:
        managed = True
        db_table = 'demo'
        verbose_name_plural = 'demo'
        verbose_name = 'demo'

    def __str__(self):
        return self.name + ' 次序' + str(self.Order)
