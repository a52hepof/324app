# Generated by Django 4.0.3 on 2022-10-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0020_alter_activity_files_alter_activity_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='files',
            field=models.FileField(default='', upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='images',
            field=models.ImageField(default='', upload_to='Actividades/'),
        ),
    ]
