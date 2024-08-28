from django.contrib import admin
from .models import Food, Store

# Registra el modelo Food
admin.site.register(Food)

# Registra el modelo Store
admin.site.register(Store)

# mi_primera_comida = Food()
# print(mi_primera_comida)