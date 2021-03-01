from django.db import models


class City(models.Model):
    city_name = models.CharField(verbose_name="City name", max_length=256)  # По сведениям из
    # интернета самое
    # длинное название города - 167 символов, берём с запасом

    def __str__(self):
        return self.city_name
