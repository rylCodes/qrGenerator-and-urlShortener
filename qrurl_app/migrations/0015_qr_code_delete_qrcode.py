# Generated by Django 4.2.1 on 2023-05-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0014_remove_qrcode_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qr_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('alias', models.CharField(max_length=200, null=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
        migrations.DeleteModel(
            name='QRCode',
        ),
    ]
