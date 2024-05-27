from django.http import HttpResponseBadRequest, HttpResponse
from http import HTTPStatus
from django.views import View
from .serialisers import validate_request
from pydantic import ValidationError
from .utils import save_data
from django.db import IntegrityError
from .models import Cab

class Register(View):

    def post(self, request):
        body = request.body
        if body.get("type", "") == "" or body.get("type", "") == None:
            return HttpResponseBadRequest(content=f'type cannot be empty not allowed')
        try:
            body = validate_request(body)
        except ValidationError as e:
            return HttpResponseBadRequest(content=e.errors())
        
        try:
            save_data(**body)
        except IntegrityError as e:
            return HttpResponseBadRequest(content=str(e))
        return HttpResponse(status=HTTPStatus.CREATED)

class UpdateLocation(View):
    def put(self, request):
        cab_id = request.params.get("cab_id")
        lat, long = request.params.get("latitude"), request.params.get("longitude")
        error_message = ""
        if cab_id == "" or cab_id == None:
            error_message = "cab_id cannot be empty"
        if lat == None or long == None:
            error_message = "Valid values of latitude and longitude should be provided"
        if error_message:
            return HttpResponseBadRequest(content=error_message)
        cab = Cab.objects.get_or_create(id=cab_id)
        cab.latitude = lat
        cab.longitude = long
        cab.save()
        return HttpResponse(content="success", status=HTTPStatus.OK)
