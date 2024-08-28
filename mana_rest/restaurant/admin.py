from django.contrib import admin
from .models import Food, Store, Ticket, TicketItem

# Registra el modelo Food
admin.site.register(Food)

# Registra el modelo Store
admin.site.register(Store)

# Registra el modelo Ticket
admin.site.register(Ticket)

# Registra el modelo TicketItem
admin.site.register(TicketItem)