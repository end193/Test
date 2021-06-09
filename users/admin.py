from django.contrib import admin
from .models import Order
from .models import StatusOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('client', 'phone_number', 'description', 'date', 'status',)


@admin.register(StatusOrder)
class StatusAdmin(admin.ModelAdmin):

    list = ('title',)