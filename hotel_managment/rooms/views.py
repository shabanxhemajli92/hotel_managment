from django.shortcuts import render, redirect
from .models import Client, Room, Booking
from datetime import datetime
from django.core.exceptions import ValidationError
from .forms import ClientForm,RoomForm

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room_number = form.cleaned_data['room_number']
            room_type = form.cleaned_data['room_type']
            price = form.cleaned_data['price']
            room = Room.objects.create(room_number=room_number, room_type=room_type, price=price)
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'rooms/room_form.html', {'form': form})

def room_list(request):
    rooms = Room.objects.all()
    room_type = request.GET.get('room_type')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    if price_min:
        rooms = rooms.filter(price__gte=price_min)
    if price_max:
        rooms = rooms.filter(price__lte=price_max)
    return render(request, 'rooms/room_list.html', {'rooms': rooms})



def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['name']
            client_email = form.cleaned_data['email']
            client_phone = form.cleaned_data['phone_number']
            client = Client.objects.create(name=client_name, email=client_email,phone_number=client_phone)
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'rooms/client_form.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'rooms/client_list.html', {'clients': clients})

def client_update(request, client_id):
    client = Client.objects.get(pk=client_id)
    if request.method == 'POST':
        client.name = request.POST['name']
        client.email = request.POST['email']
        client.phone_number = request.POST['phone_number']
        client.save()
        return redirect('client_list')
    return render(request, 'rooms/client_form.html', {'client': client})

def client_delete(request, client_id):
    client = Client.objects.get(pk=client_id)
    client.delete()
    return redirect('client_list')




def room_update(request, room_id):
    room = Room.objects.get(pk=room_id)
    if request.method == 'POST':
        room.room_number = request.POST['room_number']
        room.room_type = request.POST['room_type']
        room.price = request.POST['price']
        room.save()
        return redirect('room_list')
    return render(request, 'rooms/room_form.html', {'room': room})

def room_delete(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.delete()
    return redirect('room_list')

def is_room_available(room, check_in_date, check_out_date):
    bookings = Booking.objects.filter(room=room)
    for booking in bookings:
        if (check_in_date >= booking.check_in_date and check_in_date <= booking.check_out_date) or (check_out_date >= booking.check_in_date and check_out_date <= booking.check_out_date):
            raise ValidationError('The room is not available in this date range')

def booking_create(request, room_id, client_id):
    if request.method == 'POST':
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        room = Room.objects.get(pk=room_id)
        client = Client.objects.get(pk=client_id)
        format_str = '%Y-%m-%d'
        check_in_date = datetime.strptime(check_in_date, format_str)
        check_out_date = datetime.strptime(check_out_date, format_str)
        try:
            is_room_available(room, check_in_date, check_out_date)
            booking = Booking.objects.create(room=room, client=client, check_in_date=check_in_date, check_out_date=check_out_date)
            return redirect('room_list')
        except ValidationError as e:
            return render(request, 'rooms/error.html', {'message': e.message})
    else:
        room = Room.objects.get(pk=room_id)
        client = Client.objects.get(pk=client_id)
        return render(request, 'booking_form.html', {'room': room, 'client': client})