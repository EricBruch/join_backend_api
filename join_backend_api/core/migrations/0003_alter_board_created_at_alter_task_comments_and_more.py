# Generated by Django 4.1.4 on 2023-01-02 19:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_board_created_at_alter_task_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 19, 33, 59, 327972, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='comments',
            field=models.ManyToManyField(related_name='taksOfUser', through='core.TaskComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 19, 33, 59, 328299, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 19, 33, 59, 328263, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 19, 33, 59, 328841, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='TaskAssignedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.datetime(2023, 1, 2, 19, 33, 59, 329094, tzinfo=datetime.timezone.utc))),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='assignedUsers',
            field=models.ManyToManyField(related_name='tasksOfUser', through='core.TaskAssignedUser', to=settings.AUTH_USER_MODEL),
        ),
    ]