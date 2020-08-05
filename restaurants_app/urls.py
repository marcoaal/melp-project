from django.urls import path

from restaurants_app import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

urlpatterns = [
	path('restaurants', views.RestaurantsView.as_view(),name='crud_restaurants'),
]

urlpatterns = format_suffix_patterns(urlpatterns)