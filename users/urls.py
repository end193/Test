from django.contrib import admin
from django.urls import path, include

# Views ...
from .views import (
    UserLogoutView,
    UserLoginView,
    RegisterUserView,
    AccountView,
    OrderCreateView,
    OrderDeleteView
    )

app_name = 'users'

urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    # Заказы
    path('create/', OrderCreateView.as_view(), name='create'),
    path('delete/<int:pk>', OrderDeleteView.as_view(), name='delete'),
]