# Generated by Django 4.0.4 on 2022-06-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_remove_profile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='traning',
            field=models.BooleanField(default=False),
        ),
    ]