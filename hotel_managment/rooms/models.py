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

    def __str__(self):
        return f"room number: {self.room_number} room type: {self.room_type} price: {self.price}"


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Client: {self.client} room: {self.room} check in date: {self.check_in_date} check out date {self.check_out_date}"


class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"first name: {self.first_name} last name: {self.last_name} email: {self.email}"


CONDITION_CHOICES = (
    ("clean", "Clean"),
    ("not_clean", "Not Clean"),
)


class RoomHistory(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)

    def __str__(self):
        return f"room: {self.room} guest: {self.guest} check in date: {self.check_in_date} check out date: {self.check_out_date} condition: {self.condition} "
