# models.py

from django.db import models

class Hotel(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single Room'),
        ('studio', 'Studio'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    ]

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
    pool = models.BooleanField(default=False)
    room_types = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # New field for price per night
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)

    def __str__(self):
        return self.name
