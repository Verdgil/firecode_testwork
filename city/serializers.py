from rest_framework import serializers

from city.models import City


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("city_name", "id")
