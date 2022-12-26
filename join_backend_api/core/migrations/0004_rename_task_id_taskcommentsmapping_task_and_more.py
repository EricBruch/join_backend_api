# Generated by Django 4.1.4 on 2022-12-26 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_author_task_author_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcommentsmapping',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='taskcommentsmapping',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 17, 7, 17, 961943, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 17, 7, 17, 962260, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 26, 17, 7, 17, 962226, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskcommentsmapping',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 17, 7, 17, 962737, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskuserassignedmapping',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 17, 7, 17, 962983, tzinfo=datetime.timezone.utc)),
        ),
    ]