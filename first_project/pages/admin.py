from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'total_tasks', 'undone_tasks', 'recent_tasks']
    list_display_links = ['name']
    list_filter = ['owner']
    search_fields = ['name']
    readonly_fields = ['id']
    fieldsets = (
        (None, {
            "fields": (
                'id', ('name', 'owner'),
            ),
        }),
    )

    def total_tasks(self, obj: models.Project):
        return obj.tasks.count()
    total_tasks.short_description = _('total tasks')
    
    def undone_tasks(self, obj: models.Project):
        return obj.tasks.filter(is_done=False).count()
    undone_tasks.short_description = _('undone tasks')

    def recent_tasks(self, obj):
        return "; ".join(obj.tasks.order_by('-created').values_list('name', flat=True)[:3])
    recent_tasks.short_description = _('recent 3 tasks')


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_done', 'deadline', 'project', 'owner', 'created']
    list_filter = ['is_done', 'deadline', 'created']
    search_fields = ['name', 'description', 'project', 'owner__email', 'owner__username']
    list_editable = ['is_done']
    readonly_fields = ['id', 'updated', 'created']
    fieldsets = (
        (_('general').title(), {
            "fields": (
                ('name', 'deadline'), 'description', 'is_done',
            ),
        }),
        (_('ownership').title(), {
            "fields": (
                ('owner', 'project'),
            ),
        }),
        (_("temporal tracking").title(), {
            "fields": (
                'id', 'created', 'updated',
            ),
        }),
    )
    

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)
