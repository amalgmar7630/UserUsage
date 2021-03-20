from django.utils.translation import ugettext_lazy as _

from django.db import models


class UsageType(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    unit = models.CharField(_('Unit'), max_length=10, null=True)

    def __str__(self):
        return self.name
