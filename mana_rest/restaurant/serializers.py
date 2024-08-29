from rest_framework import serializers
from .models import Food, Store, TicketItem, Ticket

class FoodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Food
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class TicketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketItem
        fields = ['food', 'quantity', 'price']

class TicketSerializer(serializers.ModelSerializer):
    ticket_items = TicketItemSerializer(many=True, write_only=True)

    class Meta:
        model = Ticket
        fields = ['store', 'date', 'total', 'status', 'customer_name', 'ticket_items']

    def create(self, validated_data):
        print(validated_data)
        ticket_items_data = validated_data.pop('ticket_items', [])
        # aqui creamos un ticket que por el momento solo tiene nombre de consumidot 
        ticket = Ticket.objects.create(**validated_data)

        for item_data in ticket_items_data:
            print(item_data)
            TicketItem.objects.create(ticket=ticket, **item_data)

        return ticket
