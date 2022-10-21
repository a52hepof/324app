# Generated by Django 4.0.3 on 2022-10-20 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accessAplication', '0010_profile_familiaapellidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquiposRonda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSeccion', models.CharField(blank=True, max_length=100, null=True)),
                ('rondaSolar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccionName', models.CharField(max_length=150)),
                ('profile', models.ManyToManyField(through='Asociados.EquiposRonda', to='accessAplication.profile')),
            ],
        ),
        migrations.AddField(
            model_name='equiposronda',
            name='seccionName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asociados.seccion'),
        ),
        migrations.AddField(
            model_name='equiposronda',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessAplication.profile'),
        ),
    ]
