# Generated by Django 4.0.3 on 2022-10-22 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0008_alter_material_user_alter_material_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='material',
            name='tipoMaterial',
        ),
        migrations.RemoveField(
            model_name='revisionmaterial',
            name='resultadoRevision',
        ),
    ]