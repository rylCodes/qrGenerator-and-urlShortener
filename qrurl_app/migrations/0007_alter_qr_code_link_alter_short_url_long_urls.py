# Generated by Django 4.2.1 on 2023-05-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0006_alter_qr_code_link_alter_short_url_long_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='short_url',
            name='long_urls',
            field=models.CharField(max_length=1000),
        ),
    ]
