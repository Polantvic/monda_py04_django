from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Project(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    owner = models.ForeignKey(get_user_model, verbose_name=_("owner"),
                              on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})

    
