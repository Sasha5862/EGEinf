# Generated by Django 4.0.4 on 2022-06-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_task_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='solution',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
