from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.client_list, name="client_list"),
    path("clients/create/", views.client_create, name="client_create"),
    path("clients/<int:client_id>/update/", views.update_client, name="update_client"),
    path("rooms/", views.room_list, name="room_list"),
    path("rooms/<int:room_id>/update/", views.room_list, name="update_room"),
    path("rooms/<str:room_number>/history/", views.room_history, name="room_history"),
    path("rooms/create/", views.room_create, name="room_create"),
    path("create/", views.create_booking, name="create_booking"),
    path("view/", views.view_bookings, name="view_bookings"),
]
