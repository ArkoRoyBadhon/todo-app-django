# Generated by Django 3.1.7 on 2021-04-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0016_auto_20210418_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='topic',
        ),
        migrations.AlterField(
            model_name='todo',
            name='course',
            field=models.CharField(max_length=125, null=True),
        ),
    ]