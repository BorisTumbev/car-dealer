# Generated by Django 2.0.6 on 2018-07-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_app', '0011_auto_20180724_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default='images/default_image.jpg', upload_to='images/'),
        ),
    ]
