# Generated by Django 4.1.4 on 2022-12-18 13:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('created_at', models.DateField(default=datetime.datetime(2022, 12, 18, 13, 28, 30, 857650, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=300)),
                ('due_date', models.DateField(default=datetime.datetime(2023, 3, 18, 13, 28, 30, 857960, tzinfo=datetime.timezone.utc))),
                ('created_at', models.DateField(default=datetime.datetime(2022, 12, 18, 13, 28, 30, 857998, tzinfo=datetime.timezone.utc))),
                ('urgency', models.CharField(choices=[('URGENT', 'Urgent'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default='MEDIUM', max_length=20)),
                ('status', models.CharField(choices=[('BACKLOG', 'Backlog'), ('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('REVIEW', 'Review'), ('DONE', 'Done')], default='BACKLOG', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.board')),
            ],
        ),
        migrations.CreateModel(
            name='TaskCommentsMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateField(default=datetime.datetime(2022, 12, 18, 13, 28, 30, 858451, tzinfo=datetime.timezone.utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.ManyToManyField(related_name='comments', through='core.TaskCommentsMapping', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.task'),
        ),
    ]
