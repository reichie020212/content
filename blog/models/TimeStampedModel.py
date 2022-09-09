from django.utils import timezone
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super().save(*args, **kwargs)
