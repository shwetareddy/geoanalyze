from geoanalyzer.models import Trip
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.db import connections
from datetime import datetime

def geojson(request):
	points = Trip.objects.all()
	json = {
		"type": "FeatureCollection",
		"features": []
    }
	for point in points:
		data_point = {
			"type": "Feature",
			"id": point.id,
			"geometry": {
				"type": "Point", 
				"coordinates": [float(point.pickup_longitude), float(point.pickup_latitude)]
			}
		}
		json['features'].append(data_point)

	return JsonResponse(json)

def trips(request):
	north = request.GET.get('north', 90)
	south = request.GET.get('south', -90)
	east = request.GET.get('east', 180)
	west = request.GET.get('west', -180)

	points = Trip.objects.filter(
		pickup_latitude__lte=north, dropoff_latitude__lte=north, 
		pickup_latitude__gte=south, dropoff_latitude__gte=south,
		pickup_longitude__lte=east, dropoff_longitude__lte=east,
		pickup_longitude__gte=west, dropoff_longitude__gte=west
	)
	json = {
		"trips": []
    }
	for point in points:
		if int(datetime.strftime(point.pickup_time, "%H")) >= 6 and int(datetime.strftime(point.pickup_time, "%H")) < 12:
			time = "morning"
		elif int(datetime.strftime(point.pickup_time, "%H")) >= 12 and int(datetime.strftime(point.pickup_time, "%H")) < 16:
			time = "afternoon"
		elif int(datetime.strftime(point.pickup_time, "%H")) >= 16 and int(datetime.strftime(point.pickup_time, "%H")) < 21:
			time = "evening"
		else:
			time = "night"

		data_point = {
			"pickup": [float(point.pickup_longitude), float(point.pickup_latitude)],
			"dropoff": [float(point.dropoff_longitude), float(point.dropoff_latitude)],
			"time": time
		}
		json['trips'].append(data_point)

	return JsonResponse(json)

def geojsonjs(request):
	points = Trip.objects.all()
	json = {
		"type": "FeatureCollection",
		"features": []
    }
	for point in points:
		data_point = {
			"type": "Feature",
			"id": point.id,
			"geometry": {
				"type": "Point", 
				"coordinates": [float(point.pickup_longitude), float(point.pickup_latitude)]
			},
		}
		json['features'].append(data_point)

	data = "{0}({1});".format('data_callback', json)
	return HttpResponse(data, "text/javascript")

def get_trips_by_month(request):
	trips = Trip.objects.extra(select={
		'month': connections[Trip.objects.db].ops.date_trunc_sql('month', 'pickup_time')
	})\
	.values('month')\
	.annotate(count_items=Count('pickup_time'))

	json = {
		"data": []
	}

	for month in trips:
		data = {
			'count': month['count_items'],
			'month': datetime.strftime(datetime.strptime(month['month'], '%Y-%m-%d'), '%B')
		}
		json['data'].append(data)
	return JsonResponse(json)