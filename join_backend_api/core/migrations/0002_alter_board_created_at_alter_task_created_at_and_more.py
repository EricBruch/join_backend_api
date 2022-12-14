# Generated by Django 4.1.4 on 2023-01-08 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 17, 24, 157404, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 17, 24, 157716, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 8, 19, 17, 24, 157682, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskassigneduser',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 17, 24, 158500, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 17, 24, 158245, tzinfo=datetime.timezone.utc)),
        ),
    ]
