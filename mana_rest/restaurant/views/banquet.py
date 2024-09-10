from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..models import Banquet, BanquetItem
from ..serializers.serializer_banquet import BanquetSerializer, BanquetItemSerializer

class BanquetListCreate(generics.ListCreateAPIView):
    queryset = Banquet.objects.all()
    serializer_class = BanquetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

class BanquetItemListCreate(generics.ListCreateAPIView):
    queryset = BanquetItem.objects.all()
    serializer_class = BanquetItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()