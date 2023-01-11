from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Room, Booking, RoomHistory, Guest
from datetime import datetime
from django.core.exceptions import ValidationError
from .forms import ClientForm, RoomForm, BookingForm, UpdateClientForm


def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room_number = form.cleaned_data["room_number"]
            room_type = form.cleaned_data["room_type"]
            price = form.cleaned_data["price"]
            room = Room.objects.create(
                room_number=room_number, room_type=room_type, price=price
            )
            return redirect("room_list")
    else:
        form = RoomForm()
    return render(request, "rooms/room_form.html", {"form": form})


def room_list(request):
    if request.method == "POST":
        if "delete" in request.POST:
            room_id = request.POST.get("room_id")
            room = get_object_or_404(Room, id=room_id)
            # check for permissions
            room.delete()
        elif "update" in request.POST:
            room_id = request.POST.get("room_id")
            room = get_object_or_404(Room, id=room_id)
            # check for permissions
            form = RoomForm(request.POST, instance=room)
            if form.is_valid():
                form.save()
    rooms = Room.objects.all()
    room_type = request.GET.get("room_type")
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    if price_min:
        rooms = rooms.filter(price__gte=price_min)
    if price_max:
        rooms = rooms.filter(price__lte=price_max)
    return render(request, "rooms/room_list.html", {"rooms": rooms})


def room_history(request, room_number):
    room = get_object_or_404(Room, room_number=room_number)
    history = RoomHistory.objects.filter(room=room).order_by("-check_in_date")
    return render(
        request, "rooms/room_history.html", {"room": room, "history": history}
    )


def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data["name"]
            client_email = form.cleaned_data["email"]
            client_phone = form.cleaned_data["phone_number"]
            client = Client.objects.create(
                name=client_name, email=client_email, phone_number=client_phone
            )
            return redirect("client_list")
    else:
        form = ClientForm()
    return render(request, "rooms/client_form.html", {"form": form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, "rooms/client_list.html", {"clients": clients})


def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = UpdateClientForm(request.POST, instance=client)
        if "update" in request.POST:
            if form.is_valid():
                form.save()
                return redirect("client_list")
        elif "delete" in request.POST:
            client.delete()
            return redirect("client_list")
    else:
        form = UpdateClientForm(instance=client)
    return render(request, "rooms/update_client.html", {"form": form})


def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_bookings")
    else:
        form = BookingForm()
    return render(request, "rooms/booking_form.html", {"form": form})


def view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, "rooms/view_bookings.html", {"bookings": bookings})
