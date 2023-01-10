from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/update/<int:client_id>/', views.client_update, name='client_update'),
    path('clients/delete/<int:client_id>/', views.client_delete, name='client_delete'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/create/', views.room_create, name='room_create'),
    path('rooms/update/<int:room_id>/', views.room_update, name='room_update'),
    path('rooms/delete/<int:room_id>/', views.room_delete, name='room_delete'),
    path('booking/create/<int:room_id>/<int:client_id>/', views.booking_create, name='booking_create'),
]