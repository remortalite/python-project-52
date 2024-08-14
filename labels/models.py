from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(verbose_name=_("Имя"),
                            max_length=64)
    created_at = models.DateTimeField(verbose_name=_("Дата создания"),
                                      auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Метка")
        verbose_name_plural = _("Метки")
