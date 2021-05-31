from django.contrib import admin
from .models import PortfolioModel


@admin.register(PortfolioModel)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url_address', 'get_image', 'date')
    readonly_fields = ['get_image']
    ordering = ['date']