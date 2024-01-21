from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Travel(models.Model):

    TRIP_TYPE_CHOICES = [
        ('one_way', 'Aller simple'),
        ('round_trip', 'Aller-retour'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_point = models.CharField(max_length=255, default='')
    ending_point = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='travel_images/', null=True, blank=True)
    trip_type = models.CharField(max_length=20, choices=TRIP_TYPE_CHOICES, default='one_way')
    departure_date = models.DateField(blank=True, default=date.today)
    return_date = models.DateField(blank=True, null=True, default=date.today)

    def __str__(self):
        return self.title

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
