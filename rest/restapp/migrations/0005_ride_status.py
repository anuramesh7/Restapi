# Generated by Django 4.1.7 on 2023-08-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_ride_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
