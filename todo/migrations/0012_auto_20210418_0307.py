# Generated by Django 3.1.7 on 2021-04-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210418_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
