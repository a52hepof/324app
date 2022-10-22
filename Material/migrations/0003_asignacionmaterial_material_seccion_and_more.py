# Generated by Django 4.0.3 on 2022-10-22 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asociados', '0001_initial'),
        ('Material', '0002_remove_photomaterial_material_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsignacion', models.DateField(blank=True, max_length=100, null=True)),
                ('rondaSolar', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='seccion',
            field=models.ManyToManyField(through='Material.AsignacionMaterial', to='Asociados.seccion'),
        ),
        migrations.AddField(
            model_name='asignacionmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Material.material'),
        ),
        migrations.AddField(
            model_name='asignacionmaterial',
            name='seccionName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asociados.seccion'),
        ),
    ]