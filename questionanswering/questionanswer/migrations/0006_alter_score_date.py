# Generated by Django 3.2.8 on 2021-12-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionanswer', '0005_score_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='date',
            field=models.DurationField(),
        ),
    ]