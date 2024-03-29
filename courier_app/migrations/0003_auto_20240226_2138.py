# Generated by Django 3.2.1 on 2024-02-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier_app', '0002_shipping_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='Destination',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='Origin',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='status',
            field=models.CharField(blank=True, choices=[('prove of ownership', 'PROOF OF OWNERSHIP'), ('Tax and insurance', 'TAX AND INSURANCE'), ('Transit', 'TRANSIT'), ('Sorting hub ', 'SORTING HUB'), ('Inspection center', 'INSPECTION CENTER')], default='prove of ownership', max_length=100, null=True),
        ),
    ]
