# Generated by Django 4.0.3 on 2022-10-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0024_remove_activity_files_remove_activity_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='files',
            field=models.FileField(default='', upload_to='Actividades/'),
        ),
    ]