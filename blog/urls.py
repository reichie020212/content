from django.urls import path
from blog.views.CarListView import CarListView
from blog.views.CarDetailView import CarDetailView
from blog.views.CarCreateView import CarCreateView
from blog.views.CarUpdateView import CarUpdateView
from blog.views.CarDeleteView import CarDeleteView
from blog.rest.views.CarListApiView import CarListApiView
from blog.rest.views.CarDetailApiView import CarDetailApiView


urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', CarUpdateView.as_view(), name="car_update"),
    path('cars/<int:pk>/delete', CarDeleteView.as_view(), name="car_delete"),
    path('cars/create', CarCreateView.as_view(), name="car_create"),
    path('api/cars', CarListApiView.as_view(), name="car_api_list"),
    path('api/cars/<int:id>', CarDetailApiView.as_view(), name="car_api_detail"),
]


