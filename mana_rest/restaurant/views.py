from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Food, Store, Ticket
from .serializers import FoodSerializer, StoreSerializer, TicketSerializer

# Vista para listar y crear Foods
class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

# Vista para listar y crear Stores
class StoreListCreate(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# Vista para listar y crear Stores
class CreateTicket(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Aquí validas y creas el ticket con sus ítems
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()