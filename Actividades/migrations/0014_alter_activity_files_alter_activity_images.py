# Generated by Django 4.0.3 on 2022-10-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0013_alter_photoactivity_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='files',
            field=models.FileField(upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='images',
            field=models.ImageField(upload_to='Actividades/'),
        ),
    ]
