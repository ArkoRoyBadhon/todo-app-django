# Generated by Django 3.1.7 on 2021-04-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210418_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
