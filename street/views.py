from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from street.serializers import StreetListSerializer
from street.models import Street
from city.models import City


class StreetListView(ListAPIView):
    serializer_class = StreetListSerializer

    def get_queryset(self, city_pk):
        street_list_obj = Street.objects.filter(city_pk=city_pk)
        return street_list_obj

    def list(self, request, **kwargs):
        queryset = self.get_queryset(kwargs["city_pk"])
        serializer = StreetListSerializer(queryset, many=True)
        return Response(serializer.data)
