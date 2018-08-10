# Generated by Django 2.0.6 on 2018-08-10 10:02

import car_dealer_app.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('object_type', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentalVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_type', models.CharField(choices=[('A', 'Automobile'), ('M', 'Motorcycle'), ('B', 'Bus'), ('T', 'Truck')], max_length=1)),
                ('engine_type', models.CharField(choices=[('D', 'Disel'), ('P', 'Petrol'), ('E', 'Electric'), ('H', 'Hybrid')], max_length=1)),
                ('transmission', models.CharField(choices=[('A', 'Auto'), ('M', 'Manual'), ('S', 'Semi-auto')], max_length=1)),
                ('condition', models.CharField(choices=[('N', 'New'), ('U', 'Used')], max_length=1)),
                ('reg_number', models.CharField(default='', max_length=10, unique=True)),
                ('year', models.PositiveIntegerField(null=True, validators=[car_dealer_app.validators.curr_year_validator])),
                ('image', models.ImageField(default='images/default_image.jpg', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(default='')),
                ('rental_price_per_day', models.PositiveIntegerField()),
                ('rental_status', models.BooleanField(default=False)),
                ('rented_at', models.DateTimeField(default=None, null=True)),
                ('rented_until', models.DateTimeField(default=None, null=True, validators=[car_dealer_app.validators.curr_day_validator])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SellVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_type', models.CharField(choices=[('A', 'Automobile'), ('M', 'Motorcycle'), ('B', 'Bus'), ('T', 'Truck')], max_length=1)),
                ('engine_type', models.CharField(choices=[('D', 'Disel'), ('P', 'Petrol'), ('E', 'Electric'), ('H', 'Hybrid')], max_length=1)),
                ('transmission', models.CharField(choices=[('A', 'Auto'), ('M', 'Manual'), ('S', 'Semi-auto')], max_length=1)),
                ('condition', models.CharField(choices=[('N', 'New'), ('U', 'Used')], max_length=1)),
                ('reg_number', models.CharField(default='', max_length=10, unique=True)),
                ('year', models.PositiveIntegerField(null=True, validators=[car_dealer_app.validators.curr_year_validator])),
                ('image', models.ImageField(default='images/default_image.jpg', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(default='')),
                ('price', models.PositiveIntegerField(null=True)),
                ('sell_status', models.CharField(choices=[('A', 'Active'), ('S', 'Sold'), ('P', 'Pending'), ('N', 'Neutral')], default='A', max_length=1)),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='car_dealer_app.Make')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_app.Model')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
