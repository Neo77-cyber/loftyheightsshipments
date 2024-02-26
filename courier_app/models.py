from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ('prove of ownership', 'PROOF OF OWNERSHIP'),
    ('Tax and insurance', 'TAX AND INSURANCE'),
    ('Transit', 'TRANSIT'),
    ('Sorting hub ', 'SORTING HUB'),
    ('Inspection center', 'INSPECTION CENTER'),
    

)


class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null = True)
    tracking_number = models.IntegerField(blank=True, null=True)
    weight_in_kg = models.IntegerField()
    length_in_cm = models.IntegerField()
    height_in_cm = models.IntegerField()
    width_in_cm = models.IntegerField()
    name_of_shipper = models.CharField(max_length=500)
    Recievers_name = models.CharField(max_length=500)
    product = models.CharField(max_length=500)
    Origin = models.CharField(max_length=500)
    Destination = models.CharField(max_length=500)
    Departure_time = models.TimeField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null= True)
    pickup_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default = 'prove of ownership', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.tracking_number)