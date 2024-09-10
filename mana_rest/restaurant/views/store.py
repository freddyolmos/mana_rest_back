from rest_framework import generics
from ..models import Store
from ..serializers.serializer_catalog import StoreSerializer


class StoreListCreate(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer