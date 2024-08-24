# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leukemia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetail',
            name='id',
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='PatientID',
            field=models.IntegerField(default=99999, serialize=False, primary_key=True),
        ),
    ]
