from django.db import models

class Trip(models.Model):
	pickup_time = models.DateTimeField()
	pickup_latitude = models.DecimalField(max_digits=9, decimal_places=6)
	pickup_longitude = models.DecimalField(max_digits=9, decimal_places=6)
	dropoff_latitude = models.DecimalField(max_digits=9, decimal_places=6)
	dropoff_longitude = models.DecimalField(max_digits=9, decimal_places=6)

	def __unicode__(self):
		return "{0}".format(self.pickup_time)
