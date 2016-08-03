# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galletas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.SmallIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='galletas',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Proveedor'),
        ),
        migrations.AddField(
            model_name='galletas',
            name='sabores',
            field=models.ManyToManyField(to='reporter.Sabor'),
        ),
    ]