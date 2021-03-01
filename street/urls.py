from django.urls import include, path

from street.views import StreetListView

urlpatterns = [
    path('<int:city_pk>/street/', StreetListView.as_view()),
]
