from django.urls import path
from django.conf.urls import url

from restaurants_app import views


urlpatterns = [ 
    url(r'^restaurants-view$', views.RestaurantsViewList.as_view()),
    url(r'^restaurants-view/(?P<pk>\S+)', views.RestaurantsViewDetail.as_view()),
    url(r'^restaurants/statistics/$',views.RestaurantsViewCircle.as_view())
]