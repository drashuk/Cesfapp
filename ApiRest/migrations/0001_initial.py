# Generated by Django 4.0.4 on 2022-06-21 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('diagnostico', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('dosis', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescripcion',
            fields=[
                ('id_prescripcion', models.IntegerField(primary_key=True, serialize=False)),
                ('dosis', models.CharField(default='0', max_length=50)),
                ('frecuencia', models.CharField(default='0', max_length=50)),
                ('entregado', models.BooleanField(default=False)),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='ApiRest.ficha')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescripciones', to='ApiRest.medicamento')),
            ],
        ),
    ]