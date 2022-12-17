# Generated by Django 4.1.4 on 2022-12-17 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_board_created_at_alter_task_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 16, 49, 44, 140393, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 16, 49, 44, 140714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 16, 49, 44, 140677, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskusercommentmapping',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 16, 49, 44, 141069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskuserisassignedmapping',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 16, 49, 44, 141326, tzinfo=datetime.timezone.utc)),
        ),
    ]
