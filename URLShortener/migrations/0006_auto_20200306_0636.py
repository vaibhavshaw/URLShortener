# Generated by Django 2.2.2 on 2020-03-06 01:06

import URLShortener.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLShortener', '0005_auto_20200306_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortendb',
            name='url',
            field=models.CharField(max_length=500, validators=[URLShortener.validators.validate_url]),
        ),
    ]
