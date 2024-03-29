# Generated by Django 3.2.1 on 2024-02-25 00:07

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.IntegerField(blank=True, null=True)),
                ('weight_in_kg', models.IntegerField()),
                ('length_in_cm', models.IntegerField()),
                ('height_in_cm', models.IntegerField()),
                ('width_in_cm', models.IntegerField()),
                ('name_of_shipper', models.CharField(max_length=500)),
                ('Recievers_name', models.CharField(max_length=500)),
                ('product', models.CharField(max_length=500)),
                ('Origin', django_countries.fields.CountryField(max_length=2)),
                ('Destination', django_countries.fields.CountryField(max_length=2)),
                ('Departure_time', models.TimeField(blank=True, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('awaiting payment', 'AWAITING PAYMENT'), ('consignment booked', 'CONSIGNMENT BOOKED'), (' delivery scheduled', 'DELIVERY SCHEDULED'), ('customs clearance', 'CUSTOMS CLEARANCE'), ('delay. temporary volume surge', 'DELAY. TEMPORARY VOLUME SURGE'), ('collected by customer at office', 'COLLECTED BY CUSTOMER AT OFFICE')], default='awaiting payment', max_length=100, null=True)),
            ],
        ),
    ]
