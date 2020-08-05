from restaurants_app.models import Restaurants

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance  

from django.db.models import Avg, StdDev

class SpatialRestaurants:
    @staticmethod
    def get_restaurants_circle(latitude,longitude,radius):
        point = Point(longitude, latitude)
        restaurants = Restaurants.objects.filter(location__distance_lt=(
            point, Distance(m=radius)))

        count_restaurants = restaurants.count()

        avg_rating_restaurants = "-"
        stddev_rating_restaurants = "-"
        
        if restaurants:
            avg_rating_restaurants = restaurants.aggregate(Avg('rating'))['rating__avg']
            stddev_rating_restaurants = restaurants.aggregate(StdDev('rating'))['rating__stddev']

        restaurants_circle_response = {
        "count":count_restaurants,
        "avg":avg_rating_restaurants,
        "std":stddev_rating_restaurants
        }

        return restaurants_circle_response