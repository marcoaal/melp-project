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

    def post(self, request, format=None):
        try:
            restaurants_serializer = RestaurantsSerializer(data=request.data,
                context={"lat":request.data["lat"],"lng":request.data["lng"]})
            if restaurants_serializer.is_valid():
                restaurants_serializer.save()
                return Response(restaurants_serializer.data, status=status.HTTP_201_CREATED)
            return Response(restaurants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            restaurants =  Restaurants.objects.get(pk=pk)
            request.data["id"] = restaurants.id
            
            lat = request.data.get("lat",restaurants.location.y)
            lng = request.data.get("lng",restaurants.location.x)

            restaurants_serializer = RestaurantsSerializer(restaurants, data=request.data,
                context={"lat":lat,"lng":lng})
            
            if restaurants_serializer.is_valid():
                restaurants_serializer.save()
                return Response(restaurants_serializer.data)
            return Response(restaurants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Restaurants.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)