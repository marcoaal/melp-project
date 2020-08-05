from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from restaurants_app.models import Restaurants
from restaurants_app.serializers import RestaurantsSerializer


class RestaurantsView(APIView):
    def get(self, request, pk, format=None):
        try:
            restaurants =  Restaurants.objects.get(pk=pk)
            restaurants_serializer = RestaurantsSerializer(restaurants)
            return Response(restaurants_serializer.data,status=status.HTTP_200_OK)

        except Restaurants.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
