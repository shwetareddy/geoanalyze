from django.conf.urls import url, include
from geoanalyzer.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]