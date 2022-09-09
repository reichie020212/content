from django import forms
from blog.models.Car import Car


class CarForm(forms.Form):
    model = Car
    fields = (
        'name'
    )
