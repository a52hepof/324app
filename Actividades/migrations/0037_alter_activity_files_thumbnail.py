# Generated by Django 4.0.3 on 2022-10-13 19:14

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0036_alter_activity_fecha_evaluacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='files_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='Actividades/'),
        ),
    ]
