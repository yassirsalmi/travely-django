from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

class PackageReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=50)
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    departure_date = models.DateField(default=date.today)
    return_date = models.DateField(blank=True, null=True)
    hotel_name = models.CharField(max_length=255)
    duration_of_stay = models.IntegerField(default=3) 
    city_image = models.ImageField(upload_to='city_images/', null=True, blank=True)
    hotel_image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Package Reservation for {self.user.username}"

class ReservationProcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package_reservation = models.ForeignKey(PackageReservation, on_delete=models.CASCADE)
    credit_card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Reservation Process for {self.package_reservation} by {self.user.username}"
