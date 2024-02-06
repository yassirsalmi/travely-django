from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from travely_travels.models import Travel
from travely_hotels.models import Hotel

User = get_user_model()

class HotelReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    credit_card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Hotel reservation for {self.user.username}"

class TravelReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    credit_card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Travel reservation for {self.user.username}"


