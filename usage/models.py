from django.utils.translation import ugettext_lazy as _

from django.db import models

from config import settings


class Usage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="usages"
    )
    usage_type = models.ForeignKey(
        'usage_types.UsageType',
        on_delete=models.CASCADE,
        null=True,
        related_name="related_usages"
    )
    usage_at = models.DateTimeField(_("Usage At"))

    def __str__(self):
        return self.id
