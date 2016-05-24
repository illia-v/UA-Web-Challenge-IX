from randomslugfield import RandomSlugField

from django.db import models


class PizzaOrder(models.Model):
    slug = RandomSlugField(length=8)
    orderer_name = models.TextField()
    orderer_phone_number = models.IntegerField()
    orderer_address = models.TextField()
    pizza = models.TextField()
    drink = models.TextField()
    pizzeria = models.TextField()
    method_of_payment = models.CharField(max_length=10)
    date_of_delivery = models.DateTimeField()
    date_time_of_order = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.slug
