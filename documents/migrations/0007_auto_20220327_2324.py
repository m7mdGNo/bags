# Generated by Django 3.2.6 on 2022-03-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20220327_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancefcompany',
            name='NetAmount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='depositeAmount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='expenceAmount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='expenceNumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='idComapny',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='paymentAmount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='receivingAmount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='advancefcompany',
            name='recevingNumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='uplaodingdocument',
            name='documentNumber',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
