from django.db import models
from ..common.models import BaseModel, BaseMeta
from django.contrib.auth.models import User 
from django.utils.translation import gettext as _


class RoleChoice(models.TextChoices):
    # ADMIN = 'admin', 'Admin'
    OWNER = 'owner', 'Owner'
    USER = 'user', 'User'


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleChoice.choices)


    class Meta(BaseMeta):
        verbose_name = _('User')
        verbose_name_plural = _('Users')