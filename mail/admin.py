import time

from django.contrib import admin

# Register your models here.
from .models import MailTaskTemplate,MailTaskList
from django.utils.translation import ugettext_lazy
admin.site.site_header = 'app demo'
admin.site.site_title = 'app demo'

class MailTaskListAdmin(admin.ModelAdmin):

    # 需要显示的字段信息
    list_display = [ 'id','MailTaskTemplateId', 'AddTime','Status','BeginTime','FinishTime','Success']

    list_per_page = 20
    list_display_links = [ 'MailTaskTemplateId']
    list_filter = ['MailTaskTemplateId','AddTime','Status','Success']
    ordering = ['-AddTime']
    actions = ['mailNow','add2mailQueue']
    readonly_fields = [ 'id', 'AddTime','Status','BeginTime','FinishTime','Success','Log',
                       'CreateBy', 'CreateTime', 'UpdateBy', 'UpdateTime']
    autocomplete_fields = ['MailTaskTemplateId']

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not change:
                obj.CreateBy=request.user.username
            else:
                obj.UpdateBy=request.user.username
            super().save_model( request, obj, form, change)

    def add2mailQueue(self, request, queryset):
        try:
            action_ids=list(request.POST.getlist('_selected_action'))
            action_ids.reverse()
            # mail code here. with Celery
            from tasks import mail_task
            result=mail_task.delay(action_ids)
            self.message_user(request,f'''{result/len(action_ids)} 添加到任务队列成功。请稍后查看结果''')
        except:
            self.message_user(request,'添加到任务队列失败。')
    add2mailQueue.short_description = "添加到任务队列"

    def mailNow(self, request, queryset):
        try:
            action_ids=list(request.POST.getlist('_selected_action'))
            action_ids.reverse()
            # mail code here.
            from tasks import mail_task
            mail_task.delay(action_ids)
            self.message_user(request,'发送成功。以收件人确认收到为准')
        except:
            self.message_user(request,'出现错误。需手动确认是否发送成功')
    mailNow.short_description = "立即发送"

class MailTaskTemplateAdmin(admin.ModelAdmin):
    list_display = [ 'id','Name', 'Subject']

    list_per_page = 20
    list_display_links =  ['Name']
    search_fields = ['Name', 'Subject']
    fieldsets = (
        (None, {
            'fields': ( 'id',
                'Name', 'Subject', 'To', 'CC', 'Content',
            )
        }),
        ('其它信息', {
            'classes': ('collapse',),
            'fields': (
                'CreateBy', 'CreateTime', 'UpdateBy', 'UpdateTime',),
        }),

    )

    readonly_fields = [ 'id','CreateBy', 'CreateTime', 'UpdateBy', 'UpdateTime']
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not change:
                obj.CreateBy=request.user.username
            else:
                obj.UpdateBy=request.user.username
            super().save_model( request, obj, form, change)

admin.site.register(MailTaskTemplate,MailTaskTemplateAdmin)
admin.site.register(MailTaskList,MailTaskListAdmin)
