# Generated by Django 3.2.6 on 2022-03-22 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0021_alter_login_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 22, 22, 27, 57, 835782)),
        ),
    ]
