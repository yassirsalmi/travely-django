from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import HotelReservation, TravelReservation
from .forms import HotelReservationForm, TravelReservationForm
from travely_travels.models import Travel
from travely_hotels.models import Hotel
from django.shortcuts import redirect

@login_required
def goto_travel_reservation(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)
    form = TravelReservationForm()
    user = request.user
    print("Travel TEMPLATE View is called")
    return render(request, 'travely_reservations/travel_reservation.html', {'travel': travel, 'form': form, 'user': user})

@login_required
def goto_hotel_reservation(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    form = HotelReservationForm()
    print("Travel Reservation View is called")
    return render(request, 'travely_reservations/hotel_reservation.html', {'hotel': hotel, 'form': form})

@login_required
def hotel_reservation(request, hotel_id):
    print("inside saving form for hotel---------------------------------------------------------")
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.hotel = hotel

            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            total_price = calculate_total_price(hotel, start_date, end_date)
            reservation.total_price = total_price
            reservation.save()  
            return redirect('travely_auth:home')  
    else:
        form = HotelReservationForm()
    return render(request, 'travely_reservations/hotel_reservation.html', {'form': form, 'hotel': hotel})  

@login_required
def travel_reservation(request, travel_id):
    print("inside saving form for travel---------------------------------------------------------")
    travel = get_object_or_404(Travel, pk=travel_id)
    if request.method == 'POST':
        form = TravelReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.travel = travel

            # Calculate total price
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            total_price = calculate_total_price(travel, start_date, end_date)
            reservation.total_price = total_price

            reservation.save()
            print(form.errors)
            return redirect('travely_auth:home')
    else:
        form = TravelReservationForm()
        
    print(form.errors)
    return render(request, 'travely_reservations/travel_reservation.html', {'form': form, 'travel': travel})



def calculate_total_price(item, start_date, end_date):
    print("inside calcul price ---------------------------")
    print(item)
    print(type(item))

    if isinstance(item, Hotel):
        num_days = (end_date - start_date).days

        print("num of days -----------------",num_days)
        total_price = num_days * item.price_per_night

        print("total price --------------------------", total_price)
    elif isinstance(item, Travel):
        if item.trip_type == 'one_way':
            print("price -----------------",item.price)
            total_price = item.price
        elif item.trip_type == 'round_trip':
            total_price = item.price * 2
    else:
        total_price = 0  
    return total_price


@login_required
def reservation_success(request):
    return render(request, 'reservation_success.html')

