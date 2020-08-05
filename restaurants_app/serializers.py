from rest_framework import serializers

from restaurants_app.models import Restaurants

class RestaurantsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurants
		fields = ("id","rating","name")