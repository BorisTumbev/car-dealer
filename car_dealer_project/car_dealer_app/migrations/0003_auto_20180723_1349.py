# Generated by Django 2.0.6 on 2018-07-23 13:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_app', '0002_auto_20180723_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator('2018')]),
        ),
    ]
