# Generated by Django 4.1.4 on 2023-04-22 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_message_author_alter_board_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 10, 41, 41, 577445, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 10, 41, 41, 578890, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 10, 41, 41, 577755, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 22, 10, 41, 41, 577721, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskassigneduser',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 10, 41, 41, 578595, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 10, 41, 41, 578314, tzinfo=datetime.timezone.utc)),
        ),
    ]