# Generated by Django 4.2.1 on 2023-05-31 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0026_remove_qrcodegenerator_alias'),
    ]

    operations = [
        migrations.DeleteModel(
            name='URLshortener',
        ),
    ]
