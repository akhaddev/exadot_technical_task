from django.db import models
from django.utils.translation import gettext as _
from ..user.models import UserProfile
from ..field.models import Field
from ..common.models import BaseModel, BaseMeta




class Booking(BaseModel):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='booking_field')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='booking_user')
    start_time = models.DateTimeField()
    endi_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.user} {self.field}'
    
    class Meta(BaseMeta):
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')