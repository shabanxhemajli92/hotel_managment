from django.contrib import admin
from .models import Client, Room, Booking

admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Booking)
