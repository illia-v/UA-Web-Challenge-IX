# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('slug', models.CharField(max_length=8)),
                ('orderer_name', models.TextField()),
                ('orderer_phone_number', models.IntegerField()),
                ('orderer_address', models.TextField()),
                ('pizza', models.TextField()),
                ('drink', models.TextField()),
                ('method_of_payment', models.CharField(max_length=10)),
                ('date_of_delivery', models.DateTimeField()),
                ('date_time_of_order', models.DateTimeField()),
                ('status', models.SmallIntegerField(
                    choices=[
                        (0, 'Processing'),
                        (1, 'Preparing'),
                        (2, 'Delivering'),
                        (3, 'Delivered'),
                        (4, 'There is a problem')
                    ]
                )),
            ],
        ),
    ]
