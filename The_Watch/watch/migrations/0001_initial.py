# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-09 11:30
from __future__ import unicode_literals

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
            name='Neigborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neigborhood_name', models.CharField(max_length=30)),
                ('neigborhood_location', models.CharField(max_length=30)),
                ('neigborhood_count', models.CharField(max_length=30)),
                ('admin_foreign_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
