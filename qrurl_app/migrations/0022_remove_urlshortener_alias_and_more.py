# Generated by Django 4.2.1 on 2023-05-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrurl_app', '0021_urlshortener_shortened_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshortener',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='urlshortener',
            name='shortened_url',
        ),
        migrations.AlterField(
            model_name='urlshortener',
            name='uuid',
            field=models.CharField(max_length=20),
        ),
    ]
