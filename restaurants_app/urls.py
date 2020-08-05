from django.urls import path

from restaurants_app import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

urlpatterns = [
	#path('restaurants', views.RestaurantsView.as_view()),
	#path('restaurants/<str:pk>', views.RestaurantsView.as_view()),
	path('restaurants', views.RestaurantsViewList.as_view()),
	path('restaurants/<str:pk>', views.RestaurantsViewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)