# Generated by Django 4.0.3 on 2022-10-22 15:31

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=3000, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('num_responsables', models.IntegerField(default=1, verbose_name='NResponsables')),
                ('num_participantes', models.IntegerField(default=2, verbose_name='NParticipantes')),
                ('tipo_actividad', models.CharField(max_length=100, null=True)),
                ('fecha_evaluacion', models.DateField(blank=True, null=True)),
                ('realizada', models.BooleanField(blank=True, default=False, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='Actividades/')),
                ('files_thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='Actividades/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoName', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Actividades.activity')),
            ],
        ),
    ]
