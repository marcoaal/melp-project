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

    def update(self, instance, validated_data):       
        instance.rating = validated_data.get('rating', instance.rating)
        instance.name = validated_data.get('name', instance.name)
        instance.site = validated_data.get('site', instance.site)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.location = Point(self.context["lng"],self.context["lat"])
        instance.save()
        return instance

    class Meta:
        model = Restaurants
        exclude = ('location',)