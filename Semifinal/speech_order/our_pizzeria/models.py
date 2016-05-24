from django.db import models


STATUS_CHOICES = (
    (0, 'Processing'),
    (1, 'Preparing'),
    (2, 'Delivering'),
    (3, 'Delivered'),
    (4, 'There is a problem')
)


class Order(models.Model):
    slug = models.CharField(max_length=8)
    orderer_name = models.TextField()
    orderer_phone_number = models.IntegerField()
    orderer_address = models.TextField()
    pizza = models.TextField()
    drink = models.TextField()
    method_of_payment = models.CharField(max_length=10)
    date_of_delivery = models.DateTimeField()
    date_time_of_order = models.DateTimeField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.slug
