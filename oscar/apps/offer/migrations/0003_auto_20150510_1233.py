# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20150505_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='type',
            field=models.CharField(blank=True, max_length=128, verbose_name='Type', choices=[(b'Percentage', "Discount is a percentage off of the product's value"), (b'Absolute', "Discount is a fixed amount off of the product's value")]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='range',
            name='is_public',
            field=models.BooleanField(default=False, help_text='Public ranges have a customer-facing page', verbose_name='Is public?'),
            preserve_default=True,
        ),
    ]
