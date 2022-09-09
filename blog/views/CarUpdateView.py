from django.urls import reverse
from django.views.generic.edit import UpdateView
from blog.models.Car import Car


class CarUpdateView(UpdateView):
    model = Car
    fields = ['name']
    template_name = "car_form.html"

    def get_success_url(self):
        return reverse('car_list')
