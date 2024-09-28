from rest_framework import serializers
from restaurant.models import  Food, Store

class FoodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Food
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class FoodSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['title', 'price', 'image', 'discount']