from rest_framework import generics
from ..models import Food
from ..serializers.serializer_catalog import  FoodSerializer

class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer