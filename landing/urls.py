from django.contrib import admin
from django.urls import path, include

# Views ...
from .views import (
    LandingView,
    )

app_name = 'landing'

urlpatterns = [
    path('', LandingView.as_view(), name='index'),
]