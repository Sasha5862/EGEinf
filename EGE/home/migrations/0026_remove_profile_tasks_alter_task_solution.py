# Generated by Django 4.0.4 on 2022-06-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_profile_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tasks',
        ),
        migrations.AlterField(
            model_name='task',
            name='solution',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]