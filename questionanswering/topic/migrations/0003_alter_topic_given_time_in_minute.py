# Generated by Django 3.2.8 on 2021-12-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_alter_topic_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='given_time_in_minute',
            field=models.PositiveIntegerField(max_length=50, verbose_name='given time'),
        ),
    ]
