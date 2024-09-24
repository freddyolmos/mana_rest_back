from rest_framework import serializers
from restaurant.models import Ticket, TicketItem


class TicketItemSerializer(serializers.ModelSerializer):
    food_title = serializers.CharField(source='food.title', read_only=True)

    class Meta:
        model = TicketItem
        fields = ['food', 'food_title', 'quantity', 'price', 'discount']


# class CategorizedTicketItemsSerializer(serializers.Serializer):
#     category = serializers.CharField()
#     items = TicketItemSerializer(many=True)


class TicketSerializer(serializers.ModelSerializer):
    ticket_items = TicketItemSerializer(many=True, write_only=True)
    categorized_items = serializers.SerializerMethodField(read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Ticket
        fields = ['store', 'date', 'status', 'customer_name', 'ticket_items', 'categorized_items', 'total']

    def create(self, validated_data):
        ticket_items_data = validated_data.pop('ticket_items', [])

        ticket = Ticket.objects.create(**validated_data)

        total_price = 0
        categorized_items = {}

        for item_data in ticket_items_data:
            food = item_data['food']
            quantity = item_data['quantity']
            price = food.price
            discount = item_data.get('discount', 0)
            item_total = (price - discount) * quantity

            category = food.category
            if category not in categorized_items:
                categorized_items[category] = []

            categorized_items[category].append({
                'food': food,
                'quantity': quantity,
                'price': price,
                'discount': discount,
                'item_total': item_total
            })

            item_data.pop('price', None) 
            TicketItem.objects.create(
                ticket=ticket,
                price=item_total,
                **item_data
            )

            total_price += item_total

        ticket.total = total_price
        ticket.save()

        return ticket

    def get_categorized_items(self, obj):
        """
        Este método organiza los TicketItems por categoría.
        """
        categorized_items = {}
        ticket_items = TicketItem.objects.filter(ticket=obj)

        for item in ticket_items:
            category = item.food.category
            if category not in categorized_items:
                categorized_items[category] = []
            categorized_items[category].append(TicketItemSerializer(item).data)

        return [
            {"category": category,"items": items} for category, items in categorized_items.items()
        ]

