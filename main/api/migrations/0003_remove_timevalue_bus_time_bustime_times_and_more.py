# Generated by Django 4.2 on 2023-05-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_timevalue_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timevalue',
            name='bus_time',
        ),
        migrations.AddField(
            model_name='bustime',
            name='times',
            field=models.ManyToManyField(to='api.timevalue'),
        ),
        migrations.AlterField(
            model_name='timevalue',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]
