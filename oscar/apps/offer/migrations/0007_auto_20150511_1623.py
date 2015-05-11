# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0006_auto_20150511_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditionaloffer',
            name='max_basket_applications',
            field=models.PositiveIntegerField(help_text='The number of times this offer can be applied to a basket (and order)', null=True, verbose_name='Max basket applications', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conditionaloffer',
            name='max_discount',
            field=models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text='When an offer has given more discount to orders than this threshold, then the offer becomes unavailable', null=True, verbose_name='Max discount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conditionaloffer',
            name='max_global_applications',
            field=models.PositiveIntegerField(help_text='The number of times this offer can be used before it is unavailable', null=True, verbose_name='Max global applications', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conditionaloffer',
            name='max_user_applications',
            field=models.PositiveIntegerField(help_text='The number of times a single user can use this offer', null=True, verbose_name='Max user applications', blank=True),
            preserve_default=True,
        ),
    ]
