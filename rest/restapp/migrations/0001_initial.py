# Generated by Django 4.1.7 on 2023-05-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_desc', models.CharField(max_length=200)),
                ('date_Created', models.DateField(auto_now=True)),
            ],
        ),
    ]
