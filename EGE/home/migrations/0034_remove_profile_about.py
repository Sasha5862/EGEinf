# Generated by Django 4.0.4 on 2022-06-25 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_About'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
    ]
