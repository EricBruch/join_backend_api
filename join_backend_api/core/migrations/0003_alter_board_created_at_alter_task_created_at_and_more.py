# Generated by Django 4.1.4 on 2023-01-08 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_board_created_at_alter_task_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 36, 2, 953313, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 36, 2, 953687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 8, 19, 36, 2, 953653, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskassigneduser',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 36, 2, 954436, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 19, 36, 2, 954188, tzinfo=datetime.timezone.utc)),
        ),
    ]
