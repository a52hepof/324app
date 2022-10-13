# Generated by Django 4.0.3 on 2022-10-12 14:15

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0015_alter_activity_files_alter_activity_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='photoactivity',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
