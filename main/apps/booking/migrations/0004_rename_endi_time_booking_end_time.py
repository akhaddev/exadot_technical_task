# Generated by Django 4.1.5 on 2024-11-15 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='endi_time',
            new_name='end_time',
        ),
    ]
