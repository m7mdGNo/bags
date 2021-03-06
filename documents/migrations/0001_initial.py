# Generated by Django 4.0.3 on 2022-03-23 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advanceFcompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('idComapny', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('recevingNumber', models.CharField(max_length=100)),
                ('receivingAmount', models.CharField(max_length=100)),
                ('expenceNumber', models.CharField(max_length=100)),
                ('expenceAmount', models.CharField(max_length=100)),
                ('depositeAmount', models.CharField(max_length=100)),
                ('paymentAmount', models.CharField(max_length=100)),
                ('DepPayDate', models.DateField()),
                ('FCompany', models.CharField(max_length=200)),
                ('RecLink', models.CharField(max_length=200)),
                ('NetAmount', models.IntegerField(default=0, null=True)),
                ('receiDepPay', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='newFCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('FCompany', models.CharField(max_length=200)),
                ('depostieAmount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('paymenetAmount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('DepPAyDate', models.DateField()),
                ('netAmount', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='uplaodingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentNumber', models.BigIntegerField(null=True)),
                ('DocumentType', models.CharField(max_length=200)),
                ('itemType', models.CharField(max_length=200)),
                ('documentDate', models.DateField(default=datetime.datetime.today)),
                ('documentFile', models.FileField(upload_to='static')),
            ],
        ),
    ]
