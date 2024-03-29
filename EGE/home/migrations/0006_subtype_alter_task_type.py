# Generated by Django 4.0.4 on 2022-05-29 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_typetask_complexity'),
    ]

    operations = [
        migrations.CreateModel(
            name='subType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.typetask')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.subtype'),
        ),
    ]
