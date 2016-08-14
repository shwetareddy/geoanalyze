from django.shortcuts import render
from geoanalyzer.models import Trip

def index(request):
	trips = Trip.objects.all()
	context = {
		'total_trips': trips.count,
	}

	return render(request, 'geoanalyzer/index.html', context)