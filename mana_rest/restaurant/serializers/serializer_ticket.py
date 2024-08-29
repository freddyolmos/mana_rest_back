from rest_framework import serializers
from restaurant.models import Ticket, TicketItem


class TicketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketItem
        fields = ['food', 'quantity']

class TicketSerializer(serializers.ModelSerializer):
    ticket_items = TicketItemSerializer(many=True, write_only=True)

    class Meta:
        model = Ticket
        fields = ['store', 'date', 'total', 'status', 'customer_name', 'ticket_items']

    def create(self, validated_data):
        print(f"->>>> {validated_data}")
        ticket_items_data = validated_data.pop('ticket_items', [])
        # aqui creamos un ticket
        ticket = Ticket.objects.create(**validated_data)
        print(f"la fdata validada es {validated_data}")
        for item_data in ticket_items_data:
            food = item_data['food']
            quantity = item_data['quantity']
            price = food.price
            print(item_data)
            # TicketItem.objects.create(
            # ticket=ticket, 
            # price=123,
            # food=1,
            # quantity=12
            # )
            TicketItem.objects.create(
                ticket=ticket, 
                price= price*quantity,
                **item_data)

        return ticket
