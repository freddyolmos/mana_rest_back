from django.contrib import admin
from .models import Food, Store, Ticket, TicketItem

# Registra el modelo Food
admin.site.register(Food)

# Registra el modelo Store
admin.site.register(Store)

class TicketItemInline(admin.TabularInline):
    model = TicketItem
    extra = 1  # Número de formularios vacíos que se mostrarán

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'date', 'total', 'status', 'customer_name')
    inlines = [TicketItemInline]  # Añade el inline para TicketItem



# Registra el modelo Ticket
admin.site.register(Ticket, TicketAdmin)

# Registra el modelo TicketItem
admin.site.register(TicketItem)

