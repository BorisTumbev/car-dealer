# Generated by Django 2.0.6 on 2018-07-24 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_app', '0009_vehicle_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='User',
            new_name='user',
        ),
    ]
