# Generated by Django 4.2.1 on 2023-05-08 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
    ]
