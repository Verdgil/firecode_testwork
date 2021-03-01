from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from city.serializers import CityListSerializer
from city.models import City


class CityListView(ListAPIView):
    serializer_class = CityListSerializer

    def get_queryset(self):
        city_list_obj = City.objects.all()
        return city_list_obj

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = CityListSerializer(queryset, many=True)
        return Response(serializer.data)
