# Generated by Django 4.0.3 on 2022-10-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='image',
        ),
        migrations.AddField(
            model_name='activity',
            name='images',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]