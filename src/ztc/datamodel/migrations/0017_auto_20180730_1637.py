# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-30 14:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0016_auto_20180725_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaaktype',
            name='doorlooptijd_behandeling',
        ),
        migrations.RemoveField(
            model_name='zaaktype',
            name='servicenorm_behandeling',
        ),
    ]
