# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogReg', '0010_user_poked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='poked',
            field=models.ManyToManyField(related_name='_user_poked_+', to='LogReg.User'),
        ),
    ]