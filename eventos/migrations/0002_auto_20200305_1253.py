# Generated by Django 3.0.3 on 2020-03-05 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='localidades',
        ),
        migrations.AddField(
            model_name='estadio',
            name='max_capacidad',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='localidadevento',
            name='aforo',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='localidadevento',
            name='localidad',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='LocalidadEstadio',
        ),
    ]
