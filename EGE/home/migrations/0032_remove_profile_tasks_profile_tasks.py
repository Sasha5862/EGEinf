# Generated by Django 4.0.4 on 2022-06-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_profile_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tasks',
        ),
        migrations.AddField(
            model_name='profile',
            name='tasks',
            field=models.ManyToManyField(blank=True, default=None, to='home.task'),
        ),
    ]
