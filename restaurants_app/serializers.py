from rest_framework import serializers

from restaurants_app.models import Restaurants

from django.contrib.gis.geos import Point

class RestaurantsSerializer(serializers.ModelSerializer):
    lat = serializers.SerializerMethodField()
    lng = serializers.SerializerMethodField()

    def get_lat(self,obj):
        return obj.location.y

    def get_lng(self,obj):
        return obj.location.x

    def create(self, validated_data):
        validated_data["location"] = Point(self.context["lng"],self.context["lat"])
        return Restaurants.objects.create(**validated_data)

    class Meta:
        model = Restaurants
        exclude = ('location',)