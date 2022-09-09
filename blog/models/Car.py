from django.db import models
from blog.models.TimeStampedModel import TimeStampedModel


class Car(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

