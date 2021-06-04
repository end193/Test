from django.contrib import admin
from django.urls import path, include

# Views ...
from .views import (
    NewsListView,
    )

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
]