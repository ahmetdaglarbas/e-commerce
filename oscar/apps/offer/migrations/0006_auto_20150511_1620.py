# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_auto_20150510_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conditionaloffer',
            name='max_basket_applications',
        ),
        migrations.RemoveField(
            model_name='conditionaloffer',
            name='max_discount',
        ),
        migrations.RemoveField(
            model_name='conditionaloffer',
            name='max_global_applications',
        ),
        migrations.RemoveField(
            model_name='conditionaloffer',
            name='max_user_applications',
        ),
    ]
