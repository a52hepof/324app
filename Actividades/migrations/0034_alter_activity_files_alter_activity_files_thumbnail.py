# Generated by Django 4.0.3 on 2022-10-13 17:45

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0033_activity_files_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='files',
            field=models.FileField(null=True, upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='files_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='Actividades/'),
        ),
    ]
