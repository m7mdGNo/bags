# Generated by Django 4.0.3 on 2022-04-09 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0042_alter_login_last_login_alter_page_acces_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 9, 15, 14, 45, 912550)),
        ),
    ]