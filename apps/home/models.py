from django.db import models
from django.urls import reverse

from apps.apartment.models import ApartmentModel

# Create your models here.
class BookNow(models.Model):

    OPTIONS = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        )
    comnat = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE, verbose_name='apartments', null=True)
    arrivial = models.CharField(
        max_length=255
        )
    departure = models.CharField(
        max_length=255
        )
    rooms = models.CharField(max_length=255, choices=OPTIONS, null=True)
    adult = models.CharField(
        max_length=255,
        choices=OPTIONS,
        null=True
        )
    children = models.CharField(
        max_length=255,
        choices=OPTIONS,
        null=True
        )
    name = models.CharField(
        max_length=50,
    )
    surname = models.CharField(
        max_length=50,
    )
    phone = models.IntegerField()
    email = models.EmailField(
        max_length=255
        )
    

    def __str__(self):
        return f'{self.name} | {self.phone} | {self.email}'



    


