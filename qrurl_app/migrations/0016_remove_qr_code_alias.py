# Generated by Django 4.2.1 on 2023-05-30 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0015_qr_code_delete_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr_code',
            name='alias',
        ),
    ]
