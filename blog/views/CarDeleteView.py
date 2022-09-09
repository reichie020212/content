from django.urls import reverse
from django.views.generic.edit import DeleteView
from blog.models.Car import Car


class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_form.html"

    def get_success_url(self):
        return reverse('car_list')
