from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.user_create_api_view, name='user_create'),
]
