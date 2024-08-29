from django.urls import path
from .views import FoodListCreate, StoreListCreate , CreateTicket

urlpatterns = [
    path('foods/', FoodListCreate.as_view(), name='food-list-create'),
    path('stores/', StoreListCreate.as_view(), name='store-list-create'),
    path('create-ticket/', CreateTicket.as_view(), name='store-list-create'),
]
