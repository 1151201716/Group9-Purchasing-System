# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-07 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='ref_id',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
