from django.db import models

class Client(models.Model):
    app_label = "hotel_managment"
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"name: {self.name} email: {self.email} phone nr: {self.phone_number}"

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
