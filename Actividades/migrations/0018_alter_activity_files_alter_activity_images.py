# Generated by Django 4.0.3 on 2022-10-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0017_alter_photoactivity_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='files',
            field=models.FileField(null=True, upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='images',
            field=models.ImageField(null=True, upload_to='Actividades/'),
        ),
    ]