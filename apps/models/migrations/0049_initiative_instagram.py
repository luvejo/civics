# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-10-17 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0048_initiative_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='instagram',
            field=models.CharField(blank=True, help_text='Si tienes una cuenta de Instagram, pon aquí el nombre de usuario.', max_length=128, null=True, verbose_name='Instagram'),
        ),
    ]
