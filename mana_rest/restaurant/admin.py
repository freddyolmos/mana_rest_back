from django.contrib import admin
from .models import Food, Store, Ticket, TicketItem


class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'store')
    list_editable = ('price',)

# Registra el modelo Food
admin.site.register(Food, FoodAdmin)

# Registra el modelo Store
admin.site.register(Store)

class TicketItemInline(admin.TabularInline):
    model = TicketItem
    extra = 1  # Número de formularios vacíos que se mostrarán

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'date', 'status', 'customer_name', 'total')
    def calculated_total(self, obj):
        return sum(item.price for item in obj.ticketitem_set.all())

    calculated_total.short_description = 'Total'
    inlines = [TicketItemInline]  # Añade el inline para TicketItem




# Registra el modelo Ticket
admin.site.register(Ticket, TicketAdmin)

# Registra el modelo TicketItem
admin.site.register(TicketItem)

