# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import randomslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('slug', randomslugfield.fields.RandomSlugField(
                    blank=True,
                    editable=False,
                    length=8,
                    max_length=8,
                    unique=True
                )),
                ('orderer_name', models.TextField()),
                ('orderer_phone_number', models.IntegerField()),
                ('orderer_address', models.TextField()),
                ('pizza', models.TextField()),
                ('drink', models.TextField()),
                ('pizzeria', models.TextField()),
                ('method_of_payment', models.CharField(max_length=10)),
                ('date_of_delivery', models.DateTimeField()),
                ('date_time_of_order', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
