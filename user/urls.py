from django.urls import path

from . import views

urlpatterns = [
    path("register", view=views.Register.as_view(), name="register"),
    path("update_location", view=views.UpdateLocation.as_view(), name="update_view"),
]
