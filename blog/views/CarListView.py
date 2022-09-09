from django.views.generic import ListView
from blog.models.Car import Car


class CarListView(ListView):
    model = Car
    url_name = "car_list"
    queryset = model.objects.order_by('name')
    template_name = 'car_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        columns = [
            'Name',
            'Created',
            'Updated'
        ]
        context.update({
            'sadness': 'happiness',
            'columns': columns,
        })

        return context
