# Generated by Django 4.0.3 on 2022-10-22 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Supervisor')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
