from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from blog.models.Car import Car
from blog.rest.serializers.CarSerializer import CarSerializer


class CarDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Car.objects.get(id=id)
        except Car.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        instance = self.get_object(id)

        if not instance:
            return Response(
                {"res": "Car not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CarSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        instance = self.get_object(id)

        if not instance:
            return Response(
                {"res": "Car not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = {
            "name": request.data.get('name')
        }

        serializer = CarSerializer(instance=instance, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        instance = self.get_object(id)

        if not instance:
            return Response(
                {"res": "Car not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        instance.delete()
        return Response(
            {"res": "Car deleted"},
            status=status.HTTP_200_OK
        )
