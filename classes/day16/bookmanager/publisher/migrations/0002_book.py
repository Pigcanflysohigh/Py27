# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-17 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Publisher')),
            ],
        ),
    ]
