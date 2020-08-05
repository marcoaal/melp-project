from rest_framework import serializers

from restaurants_app.models import Restaurants

class RestaurantsSerializer(serializers.ModelSerializer):
	lat = serializers.SerializerMethodField()
	lng = serializers.SerializerMethodField()

	def get_lat(self,obj):
		return obj.location.y

	def get_lng(self,obj):
		return obj.location.x

	class Meta:
		model = Restaurants
		fields = ("id","rating","name","site","email","phone","street","city","state","lat","lng")