from django.urls import path
from .views.banquet import BanquetItemListCreate, BanquetListCreate
from .views.food import FoodListCreate
from .views.store import StoreListCreate
from .views.ticket import CreateTicket, GetTicket

urlpatterns = [
    path('foods/', FoodListCreate.as_view(), name='food-list-create'),
    path('stores/', StoreListCreate.as_view(), name='store-list-create'),
    path('create-ticket/', CreateTicket.as_view(), name='ticket-create'),
    path('ticket/<int:id>/', GetTicket.as_view(), name='ticket-get'),
    path('banquets/', BanquetListCreate.as_view(), name='banquet-list-create'),
    path('banquet-items/', BanquetItemListCreate.as_view(), name='banquet-item-list-create'),
]
