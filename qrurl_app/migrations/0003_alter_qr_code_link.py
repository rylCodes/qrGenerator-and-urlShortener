# Generated by Django 4.2.1 on 2023-05-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0002_qr_code_delete_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='link',
            field=models.CharField(max_length=1000),
        ),
    ]
