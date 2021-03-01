from rest_framework import serializers

from street.models import Street


class StreetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ("street_name", )
