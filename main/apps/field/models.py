from django.db import models
from ..common.models import BaseModel, BaseMeta
from utils import upload_field_images
from user.models import UserProfile


class FieldImages(BaseModel):
    image = models.ImageField(upload_to=upload_field_images)


class Field(BaseModel):
    field = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='field_owner')
    local = models.CharField(max_length=255)
    images = models.ManyToManyField(FieldImages)


    def __str__(self):
        return f'{self.user} {self.field}'
    
    class Meta(BaseMeta):
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')