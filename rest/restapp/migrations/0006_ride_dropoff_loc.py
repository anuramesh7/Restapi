# Generated by Django 4.1.7 on 2023-08-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0005_ride_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='dropoff_loc',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
