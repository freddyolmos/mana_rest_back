from django.contrib import admin
from .models import Food, Store, Ticket, TicketItem, Banquet, BanquetItem


class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'discount',)
    list_editable = ('price',)

admin.site.register(Food, FoodAdmin)

admin.site.register(Store)

class TicketItemInline(admin.TabularInline):
    model = TicketItem
    extra = 1 

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'date', 'status', 'customer_name', 'total')
    def calculated_total(self, obj):
        return sum(item.price for item in obj.ticketitem_set.all())

    calculated_total.short_description = 'Total'
    inlines = [TicketItemInline]  


admin.site.register(Ticket, TicketAdmin)

admin.site.register(TicketItem)

class BanquetItemInline(admin.TabularInline):
    model = BanquetItem
    extra = 1

class BanquetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'datetime', 'total_cost', 'store')
    inlines = [BanquetItemInline]

admin.site.register(Banquet, BanquetAdmin)
admin.site.register(BanquetItem)