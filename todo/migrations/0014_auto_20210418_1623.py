# Generated by Django 3.1.7 on 2021-04-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20210418_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='topic',
            field=models.CharField(choices=[('Course-link', 'Course-link'), ('Announcement', 'Announcement'), ('Quiz-1', 'Quiz-1'), ('Quiz-2', 'Quiz-2'), ('Quiz-3', 'Quiz-3'), ('Extra-quiz', 'Extra-quiz'), ('Assignment', 'Assignment'), ('Presentation', 'Presentation'), ('Project', 'Project'), ('Mid-exam', 'Mid-exam'), ('Final-exam', 'Final-exam')], max_length=15, null=True),
        ),
    ]
