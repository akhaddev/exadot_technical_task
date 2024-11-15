# Generated by Django 4.1.5 on 2024-11-15 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('field', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='field_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]