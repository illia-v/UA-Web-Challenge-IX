from django.contrib import admin

from .models import PizzaOrder


@admin.register(PizzaOrder)
class PizzaOrderAdmin(admin.ModelAdmin):
    ordering = ('date_of_delivery', 'date_time_of_order')
    list_display = ('slug', 'date_time_of_order', 'date_of_delivery', 'status')
