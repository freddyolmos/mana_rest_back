from rest_framework import serializers
from .models import Food, Store

class FoodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Food
        fields = ['title', 'image']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
