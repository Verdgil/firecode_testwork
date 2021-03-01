from django.db import models

from city.models import City


class Street(models.Model):
    street_name = models.CharField(verbose_name="Street name", max_length=256)
    city_pk = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_name
