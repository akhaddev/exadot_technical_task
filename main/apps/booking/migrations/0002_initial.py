# Generated by Django 4.1.5 on 2024-11-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('field', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_field', to='field.field'),
        ),
    ]
