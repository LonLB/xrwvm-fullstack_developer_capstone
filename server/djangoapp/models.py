# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # other fields as needed

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'sedan'),
        ('SUV', 'suv'),
        ('WAGON', 'wagon')
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(validators=[MinValueValidator(2015),
                                           MaxValueValidator(2023)])
    
    # any other fields needed
    def __str__(self):
        return self.name
