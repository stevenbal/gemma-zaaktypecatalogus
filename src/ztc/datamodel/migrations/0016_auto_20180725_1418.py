# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-25 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0015_auto_20180724_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogus',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True),
        ),
        migrations.AlterField(
            model_name='eigenschap',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True),
        ),
        migrations.AlterField(
            model_name='statustype',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True),
        ),
        migrations.AlterField(
            model_name='zaaktype',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True),
        ),
    ]
