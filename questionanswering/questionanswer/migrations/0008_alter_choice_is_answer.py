# Generated by Django 3.2.8 on 2021-12-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionanswer', '0007_alter_score_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_answer',
            field=models.BooleanField(default=False),
        ),
    ]