# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-02 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_feedback_api', '0013_use_full_urls'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Comparison',
        ),
    ]
