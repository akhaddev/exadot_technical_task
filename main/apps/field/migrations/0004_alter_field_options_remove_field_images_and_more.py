# Generated by Django 4.1.5 on 2024-11-15 12:35

from django.db import migrations, models
import main.apps.field.utils


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0003_alter_field_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ('-id',), 'verbose_name': 'Field', 'verbose_name_plural': 'Fields'},
        ),
        migrations.RemoveField(
            model_name='field',
            name='images',
        ),
        migrations.DeleteModel(
            name='FieldImages',
        ),
        migrations.AddField(
            model_name='field',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=main.apps.field.utils.upload_field_images),
        ),
    ]
