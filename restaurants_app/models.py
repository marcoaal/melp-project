from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurants(models.Model):
	id = models.TextField(primary_key=True, unique = True)
	rating = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(4)])
	name = models.TextField(default="")
	site = models.TextField(default="")
	email = models.TextField(default="")
	phone = models.TextField(default="")
	street = models.TextField(default="")
	city = models.TextField(default="")
	state = models.TextField(default="")
	location = models.PointField()
	#lat = models.FloatField()
	#lng = models.FloatField()
	#models.PointField()