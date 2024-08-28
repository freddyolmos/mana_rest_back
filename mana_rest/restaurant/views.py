from django.shortcuts import render

from rest_framework import generics
from .models import Food, Store
from .serializers import FoodSerializer, StoreSerializer

# Vista para listar y crear Foods
class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

# Vista para listar y crear Stores
class StoreListCreate(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
