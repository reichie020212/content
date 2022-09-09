from django.views.generic import DetailView
from blog.models.Car import Car


class CarDetailView(DetailView):
    model = Car
    url_name = "car_detail"
    template_name = "car_detail.html"
