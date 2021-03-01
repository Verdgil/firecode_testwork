from rest_framework import serializers
from rest_framework.fields import Field

from shop.models import Shop


class ShopListSerializer(serializers.ModelSerializer):
    street_name = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()

    def get_street_name(self, obj):
        return obj.street_pk.street_name

    def get_city_name(self, obj):
        return obj.street_pk.city_pk.city_name

    class Meta:
        model = Shop
        fields = ("shop_name", "street_name", "city_name",
                  "house_name", "opening_time", "closing_time", "street_pk", "pk")
        extra_kwargs = {
            'street_pk': {'write_only': True}
        }
