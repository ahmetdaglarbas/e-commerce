# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='range',
            name='is_public',
            field=models.BooleanField(default=False, help_text='Public ranges have a customer-facing page', verbose_name='Is it public?'),
            preserve_default=True,
        ),
    ]
