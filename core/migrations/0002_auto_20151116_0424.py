# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='description',
            new_name='Review',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='Track',
        ),
    ]
