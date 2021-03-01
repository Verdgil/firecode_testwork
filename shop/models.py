from django.db import models

from street.models import Street
from city.models import City


class Shop(models.Model):
    shop_name = models.CharField(verbose_name="Shop name", max_length=512)
    street_pk = models.ForeignKey(Street, on_delete=models.CASCADE)
    # city_pk решил убрать, так как в street_pk он тоже будет
    house_name = models.CharField(verbose_name="House name", max_length=64)
    opening_time = models.TimeField(verbose_name="Opening time")
    closing_time = models.TimeField(verbose_name="Closing time")

    def __str__(self):
        return self.shop_name
