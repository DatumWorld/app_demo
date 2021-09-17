from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin  # plugin for tree-style exhibition

from .models import Task



class TaskAdmin(DjangoMpttAdmin):
    tree_auto_open = True
    list_display = ( 'name','parent','Active','Order','tree_id')
    search_fields = ['name']
    list_filter = ('tree_id',)
    list_per_page = 20
    actions = ['submit_schedule']
    fieldsets = (
        (None, {
            'fields': ('id',
             'name','parent','Active','Order','tree_id',
            )
        }),
        ('任务（模板）选择', {
            'classes': ('collapse',),
            'fields': ('UnifiedTask_id',),
        }),

        ('其它信息', {
            'classes': ('collapse',),
            'fields': (
                'Description',
                     'CreateBy','CreateTime','UpdateBy','UpdateTime'
            ),
        }),
    )
    readonly_fields = ['id','tree_id', 'CreateTime', 'UpdateTime','CreateBy','UpdateBy']

    def has_change_permission(self, request, obj=None):
        request.user.is_superuser

    def submit_schedule(self,request,obj):
        try:
            from demo.tasks import share_task
            result = share_task.delay(request.user.username)
            self.message_user(request, '提交任务成功，请稍后去“任务执行状态”页面检查确认。')
        except:
            import traceback
            self.message_user(request, '提交任务失败' + traceback.format_exc())
    submit_schedule.short_description = "提交任务"

admin.site.register(Task, TaskAdmin)

