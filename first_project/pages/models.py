from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Project(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              verbose_name=_("owner"), related_name='projects')

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ["id"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})

class Task(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    description = models.TextField(_("description"), blank=True, max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                verbose_name=_("project"), related_name='tasks')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              verbose_name=_("owner"), related_name='tasks')
    created = models.DateTimeField(_("created"), auto_now_add=True, db_index=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    is_done = models.BooleanField(_("is_done"), default=False, db_index=True)
    deadline = models.DateField(_("deadline"), null=True, blank=True, db_index=True)

    

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
        ordering = ['name', 'created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
