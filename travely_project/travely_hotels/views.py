from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HotelForm
from .models import Hotel

def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.save()
            return redirect('admin_dashboard')
        else:
            print(form.errors)
    else:
        form = HotelForm()

    return render(request, 'travely_hotels/add_hotel.html', {'form': form})


@login_required
def all_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'travely_hotels/all_hotels.html', {'hotels': hotels})

def modify_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('travely_hotels:all_hotels')
    else:
        form = HotelForm(instance=hotel)

    return render(request, 'travely_hotels/modify_hotel.html', {'form': form, 'hotel': hotel})

def delete_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    hotel.delete()
    return redirect('travely_hotels:all_hotels')

def hotel_details(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'travely_Hotels/Hotel_details.html', {'hotel': hotel})
