# Generated by Django 3.2.6 on 2022-03-24 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_uplaodingdocument_documentfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uplaodingdocument',
            old_name='documentFile',
            new_name='file',
        ),
    ]
