from django.contrib import admin
from .models import ServicesModel


@admin.register(ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

