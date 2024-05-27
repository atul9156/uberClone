from .models import Trip
from django.shortcuts import get_object_or_404

def mark_trip_complete(trip_id: int):
    trip = get_object_or_404(Trip, id=trip_id)
    trip.is_completed = True
    trip.save()
    return trip.cab_id
