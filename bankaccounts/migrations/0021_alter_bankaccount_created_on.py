# Generated by Django 4.1.3 on 2022-11-26 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0020_alter_bankaccount_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 26, 2, 52, 46, 511572)),
        ),
    ]