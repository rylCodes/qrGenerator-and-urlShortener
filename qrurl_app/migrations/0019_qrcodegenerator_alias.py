# Generated by Django 4.2.1 on 2023-05-31 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0018_urlshortener_rename_qrcode_qrcodegenerator'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodegenerator',
            name='alias',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
