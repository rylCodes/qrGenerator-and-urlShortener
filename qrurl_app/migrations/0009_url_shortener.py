# Generated by Django 4.2.1 on 2023-05-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0008_delete_short_url_qr_code_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url_shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000)),
                ('uuid', models.CharField(max_length=20)),
            ],
        ),
    ]
