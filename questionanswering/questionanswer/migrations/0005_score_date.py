# Generated by Django 3.2.8 on 2021-12-13 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionanswer', '0004_auto_20211210_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
