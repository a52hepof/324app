# Generated by Django 4.0.3 on 2022-10-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='images',
            field=models.ImageField(default='', upload_to='materialCampismo/'),
        ),
    ]