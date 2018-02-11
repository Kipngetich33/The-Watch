# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0006_business_business_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
