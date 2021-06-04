from django.contrib import admin
from django.urls import path, include

# Views ...
from .views import (
    LandingView,
    ServicesListView,
    ContactView,
    )

app_name = 'landing'

urlpatterns = [
    path('', LandingView.as_view(), name='index'),
    path('services/', ServicesListView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
]