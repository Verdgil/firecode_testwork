from django.urls import include, path

from city.views import CityListView

urlpatterns = [
    path('', CityListView.as_view()),
]
