# Generated by Django 4.0.3 on 2022-10-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0039_remove_activity_realizada'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='realizada',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
