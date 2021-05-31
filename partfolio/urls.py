from django.contrib import admin
from django.urls import path, include


# Views ...
from .views import (
   PortfolioListView,
    )

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='index'),
]