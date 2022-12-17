# Generated by Django 4.1.4 on 2022-12-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_task_alter_board_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('BackLOG', 'Backlog'), ('TO_DO', 'To_do')], default='BackLOG', max_length=20),
        ),
    ]