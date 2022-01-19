from django.db import models
from django.utils.translation import gettext_lazy as _


class Activity(models.Model):

    class STATUS(models.TextChoices):
        OPEN = 'open', _('open')
        CLOSED = 'closed', _('closed')

    name = models.CharField(max_length=64)
    content = models.TextField()
    author = models.CharField(max_length=64)
    cover = models.CharField(max_length=255)
    tags = models.CharField(max_length=64)
    status = models.CharField(max_length=64, default=STATUS.OPEN)
    time_slot = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activities'
