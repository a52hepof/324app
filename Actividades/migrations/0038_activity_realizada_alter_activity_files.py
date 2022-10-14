# Generated by Django 4.0.3 on 2022-10-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0037_alter_activity_files_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='realizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activity',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='Actividades/'),
        ),
    ]
