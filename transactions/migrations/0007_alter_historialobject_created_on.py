# Generated by Django 4.1.3 on 2022-11-23 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_historialobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialobject',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 18, 10, 3, 631399)),
        ),
    ]
