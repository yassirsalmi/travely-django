from .models import CustomUser
from travely_reservations.models import TravelReservation
from django.db.models import Sum

def num_clients(request):
    num_clients = CustomUser.objects.filter(is_client=True).count()
    return {'num_clients': num_clients}

def total_reservation_price(request):
    total_price = TravelReservation.objects.aggregate(total_price=Sum('total_price'))['total_price'] or 0
    return {'total_reservation_price': total_price}
