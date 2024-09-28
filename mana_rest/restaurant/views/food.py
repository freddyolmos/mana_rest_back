from django.db.models import Sum
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Food, TicketItem
from ..serializers.serializer_catalog import  FoodSerializer, FoodSimpleSerializer

class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class TopSellingFoodView(APIView):
    def get(self, request, *args, **kwargs):
        top_selling_foods = (
            Food.objects.annotate(total_quantity_sold=Sum('ticketitem__quantity'))
            .order_by('-total_quantity_sold')[:5]
        )
        
        serializer = FoodSimpleSerializer(top_selling_foods, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)