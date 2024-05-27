from .models import Passenger, Cab
from .constants import LAT_SEARCH, LONG_SEARCH
from django.shortcuts import get_object_or_404

def save_data(type, **kwargs):
    model = Passenger if type == "passenger" else Cab
    model.objects.create(**kwargs)

def search_cabs(lat: int, long:int):
    cabs = Cab.objects.filter(Cab.latitude__range(lat + LAT_SEARCH[0], lat + LAT_SEARCH[1])).filter(Cab.longitude__range(long + LONG_SEARCH[0], lat + LONG_SEARCH[1]))
    return [cab.to_dict() for cab in cabs]

def change_cab_availability(driver_id: int):
    cab = get_object_or_404(Cab, id=driver_id)
    cab.is_available = not cab.is_available
    cab.save()

def compute_distance(pt1, pt2):
    return ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** (1/2)

def find_nearest_cab(lat: int, long:int):
    cabs = search_cabs(lat, long)
    minima = float("inf")
    res = None
    for i, cab in enumerate(cabs):
        distance = compute_distance((lat, long), (cab.get("lat"), cab.get("long")))
        if minima > distance:
            minima = distance
            res = cab.get("id")
    return res
