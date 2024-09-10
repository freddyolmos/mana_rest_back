from rest_framework import serializers
from ..models import Banquet, BanquetItem

class BanquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banquet
        fields = ['id', 'name', 
                  'description', 'event_date', 
                  'total_cost', 'store']

class BanquetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanquetItem
        fields = ['id', 'banquet', 
                  'food', 'quantity', 
                  'price_per_item', 'total_price']
