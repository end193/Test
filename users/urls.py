from django.contrib import admin
from django.urls import path, include

# Views ...
from .views import (
    UserLogoutView,
    UserLoginView,
    RegisterUserView,
    AccountView,
    )

app_name = 'users'

urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
]