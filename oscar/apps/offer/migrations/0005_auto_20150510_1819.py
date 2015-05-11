# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_auto_20150510_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condition',
            options={'verbose_name': 'Condition', 'verbose_name_plural': 'Conditions'},
        ),
        migrations.AlterField(
            model_name='conditionaloffer',
            name='condition',
            field=models.ForeignKey(verbose_name='Condition', to='offer.Condition'),
            preserve_default=True,
        ),
    ]
