from django.views import View
from django.http import HttpResponseBadRequest, HttpResponse
from http import HTTPStatus
from user.utils import search_cabs, change_cab_availability, find_nearest_cab
from .utils import mark_trip_complete
from .models import Trip
# Create your views here.

class ListCabs(View):
    def get(self, request):
        lat, long = request.params.get("latitude"), request.params.get("longitude")
        if not isinstance(lat, int) or not isinstance(long, int):
            return HttpResponseBadRequest(content="Latitude and longitude should be valid integers")
        cabs = search_cabs(lat, long)
        return HttpResponse(content=cabs, status=HTTPStatus.OK)

class BookCab(View):
    def post(self, request):
        # user sends user_id, source, destination
        # get the closest driver
        # create trip
        # send driver details to user
        # send a SSE to driver
        user_id = request.body.get("user_id")
        source = request.body.get("source")
        dest = request.body.get("destination")
        lat = request.body.get("lat")
        long = request.body.get("long")
        # TODO: add validation

        cab_id = find_nearest_cab(lat, long)
        if cab_id:
            Trip.objects.create(user_id=user_id, cab_id=cab_id)
            return HttpResponse(content=f"Cab: {cab_id}", status=HTTPStatus.OK)
        return HttpResponse(content="No cabs found", status=HTTPStatus.OK)

class CompletedTrip(View):
    def put(self, request):
        # find trip by trip id
        # mark trip complete
        # mark driver free
        # optionaly send back trip cost
        trip_id = request.body.get("trip_id")
        if not isinstance(trip_id, int):
            return HttpResponseBadRequest(content="Invalid Trip ID")
        cab_id = mark_trip_complete(trip_id)
        change_cab_availability(cab_id)
        return HttpResponse(content="$100", status=HTTPStatus.OK)

