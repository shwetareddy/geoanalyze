from django.conf.urls import url
from api.views import geojson, trips, geojsonjs, get_trips_by_month

urlpatterns = [
    url(r'^geojson$',  geojson, name='geo_json'),
    url(r'^trips$',  trips, name='trips'),
    url(r'^geojsonjs/pickups$',  geojsonjs, name='geo_json_js'),
    url(r'^trips_by_month$', get_trips_by_month, name="by_month"),
]