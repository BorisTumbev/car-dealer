# Generated by Django 2.0.6 on 2018-07-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_app', '0014_auto_20180726_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='sold_for',
        ),
        migrations.AlterField(
            model_name='make',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='sell_status',
            field=models.CharField(choices=[('A', 'Active'), ('S', 'Sold'), ('P', 'Pending'), ('N', 'Neutral')], default='A', max_length=1),
        ),
    ]