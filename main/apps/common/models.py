import uuid
import os
from django.db import models
from django.utils.translation import gettext as _



class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseMeta(object):
    ordering = ("-id",)