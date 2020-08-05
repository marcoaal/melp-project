from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from restaurants_app.models import Restaurants
from restaurants_app.serializers import RestaurantsSerializer


class RestaurantsView(APIView):
	def get(self,request):
		restaurants = Restaurants.objects.all()
		restaurants_serializer = RestaurantsSerializer(restaurants, many=True)
		return Response(restaurants_serializer.data,status=status.HTTP_200_OK)