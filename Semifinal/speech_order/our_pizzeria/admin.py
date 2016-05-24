from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('status', 'date_of_delivery', 'date_time_of_order')
    list_display = ('slug', 'date_of_delivery', 'status')
