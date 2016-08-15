from django.core.management.base import BaseCommand
from geoanalyzer.models import Trip
import csv
import urllib2
from datetime import datetime

class Command(BaseCommand):
	help = 'Loads initial data'

	def handle(self, *args, **options):
		urls = [
			'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-apr14.csv',
			'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-may14.csv',
			'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-jun14.csv',
			'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-jul14.csv',
			'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-aug14.csv',
			'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-sep14.csv',
		]

		for url in urls:
			response = urllib2.urlopen(url)
			filereader = csv.reader(response)
			header = filereader.next()

			for row in filereader:
				nextrow = filereader.next()
				date_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S')
				if nextrow:
					trip = Trip(
						pickup_time = date_object,
						pickup_latitude = row[1],
						pickup_longitude = row[2],
						dropoff_latitude = nextrow[1],
						dropoff_longitude = nextrow[2],
					)
					trip.save()

		self.stdout.write(self.style.SUCCESS('data loaded'))