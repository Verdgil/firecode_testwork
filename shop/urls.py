from django.urls import include, path

from shop.views import ShopListView

urlpatterns = [
    path('', ShopListView.as_view()),
]
