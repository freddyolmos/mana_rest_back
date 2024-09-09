from django.urls import path
from .views import BanquetItemListCreate, BanquetListCreate, FoodListCreate, StoreListCreate , CreateTicket

urlpatterns = [
    path('foods/', FoodListCreate.as_view(), name='food-list-create'),
    path('stores/', StoreListCreate.as_view(), name='store-list-create'),
    path('create-ticket/', CreateTicket.as_view(), name='store-list-create'),
    path('banquets/', BanquetListCreate.as_view(), name='banquet-list-create'),
    path('banquet-items/', BanquetItemListCreate.as_view(), name='banquet-item-list-create'),
]
