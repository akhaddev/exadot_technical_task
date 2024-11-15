from django.urls import path, include
from . import views


urlpatterns = [
    path('field-create/', views.field_create_api_view, name='field_create'),
]
