# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leukemia', '0002_auto_20180321_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetail',
            name='Result',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
    ]
