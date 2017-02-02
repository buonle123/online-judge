# -*- coding: utf-8 -*-
# Generated by Kirito Feng on shrooms
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0057_blue_pretests'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='curators',
            field=models.ManyToManyField(to='judge.Profile', verbose_name='curators', blank=True, related_name='curated_problems',
                                         help_text='These users will be able to edit a problem, but not be publicly shown as an author.')
        ),
]