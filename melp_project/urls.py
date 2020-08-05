from django.urls import include,path

urlpatterns = [
    path('', include('restaurants_app.urls')),
]