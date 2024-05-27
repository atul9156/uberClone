from django.urls import path

from . import views

urlpatterns = [
    path("list_cabs", view=views.ListCabs.as_view()),
    path("book_cab", view=views.BookCab.as_view()),
    path("complete_trip", view=views.CompletedTrip.as_view()),
]
