from datetime import datetime

from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from shop.serializers import ShopListSerializer
from shop.models import Shop


class ShopListView(ListAPIView, CreateAPIView):
    serializer_class = ShopListSerializer

    @property
    def get_queryset(self):
        shop_list_obj = Shop.objects.all()
        street = self.request.query_params.get('street', None)
        city = self.request.query_params.get('city', None)
        is_open = self.request.query_params.get('open', None)
        if street is not None:
            shop_list_obj = shop_list_obj.filter(street_pk=street)
        if city is not None:
            shop_list_obj = shop_list_obj.filter(street_pk=city)
        if is_open is not None:
            now_time = datetime.time(datetime.now())
            if is_open == "1":
                shop_list_obj = shop_list_obj.filter(
                    opening_time__lte=now_time,
                    closing_time__gte=now_time)
            elif is_open == "0":
                shop_list_obj = shop_list_obj.exclude(
                    opening_time__lte=now_time,
                    closing_time__gte=now_time)
            else:
                return Response("object not found", status.HTTP_400_BAD_REQUEST)
        return shop_list_obj

    def list(self, request, **kwargs):
        queryset = self.get_queryset
        serializer = ShopListSerializer(queryset, many=True)
        return Response(serializer.data)
