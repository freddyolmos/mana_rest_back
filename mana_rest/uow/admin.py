from django.contrib import admin
from uow.models import UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_special_discount',)
    list_editable = ('has_special_discount',)

admin.site.register(UserProfile, UserAdmin)
