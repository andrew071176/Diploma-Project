from django.urls import path
from .views import main, update_reservation, list_reservations
urlpatterns = [
    path ('', main, name='main'),
    path('manager/update_reserve/<int:pk>', update_reservation, name='update_reservation'),
    path('manager/reserve_list/', list_reservations, name='list_reservations'),
]