# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_ftp_set_unlimited_length_for_ftp_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ups',
            name='ups_shutdowntimer',
            field=models.IntegerField(default=30, help_text='The time in seconds until shutdown is initiated. If the UPS happens to come back before the time is up the shutdown is canceled.', null=True, verbose_name='Shutdown timer'),
        ),
    ]
