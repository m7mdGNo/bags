# Generated by Django 3.2.6 on 2022-03-23 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0026_alter_login_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 23, 22, 37, 18, 661151)),
        ),
    ]
