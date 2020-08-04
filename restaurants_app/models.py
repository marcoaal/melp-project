from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurants(models.Model):
	id = models.TextField(primary_key=True, unique = True)
	rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
	name = models.TextField()
	site = models.TextField()
	email = models.TextField()
	phone = models.TextField()
	street = models.TextField()
	city = models.TextField()
	state = models.TextField()
	location = models.PointField()
	#lat = models.FloatField()
	#lng = models.FloatField()
	#models.PointField()