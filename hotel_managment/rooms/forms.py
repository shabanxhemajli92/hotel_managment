from django import forms
from .models import Client, Room, Booking

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number','room_type','price']
   

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date']