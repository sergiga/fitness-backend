# Generated by Django 3.0 on 2019-12-08 16:18

import core.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device_updated', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device_updated', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(choices=[(1, 'BEGINNER'), (2, 'INTERMEDIATE'), (3, 'ADVANCED')], default=core.utils.Level['INTERMEDIATE'])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device_updated', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MuscleInExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device_updated', models.DateTimeField(null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='muscles_in_exercise', to='exercises.Exercise')),
                ('muscle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='muscles_in_exercise', to='exercises.Muscle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EquipmentInExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device_updated', models.DateTimeField(null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments_in_exercise', to='exercises.Equipment')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments_in_exercise', to='exercises.Exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
