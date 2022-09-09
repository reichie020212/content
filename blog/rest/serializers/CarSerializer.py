from rest_framework import serializers
from blog.models.Car import Car
from django.utils import timezone


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"
