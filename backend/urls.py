from django.urls import path

from .views import BeaconsView


app_name = "beacons"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('beacons/', BeaconsView.as_view()),
]