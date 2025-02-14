# Generated by Django 5.1.6 on 2025-02-14 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_description', models.TextField()),
                ('task_priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50)),
                ('task_type', models.CharField(choices=[('Individual', 'Individual'), ('Team', 'Team')], default='Individual', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(default='', max_length=100)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=50)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_given', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]
