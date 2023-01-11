from django.contrib import admin
from .models import Client, Room, Booking, RoomHistory, Guest

admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Guest)
admin.site.register(RoomHistory)
