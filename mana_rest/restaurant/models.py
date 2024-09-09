from django.db import models
from django.conf import settings
from uow.models import UserProfile

class Food(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    category = models.CharField(max_length=30, null=True, blank=True)
    is_available = models.BooleanField(default=True)  
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='foods', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    

class Store(models.Model):
    name = models.CharField(max_length=20, default='Store', null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    location = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Ticket(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='tickets')
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    STATUS_CHOICES = [
        ('PAG', 'Pagado'),
        ('PEN', 'Pendiente'),
        ('CAN', 'Cancelado'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    foods = models.ManyToManyField(Food, through='TicketItem')

    def __str__(self):
        return f"Ticket #{self.id} - {self.store} - {self.get_status_display()}"

class TicketItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantity}x {self.food.title} - Ticket #{self.ticket.id}"

class Banquet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Banquete for {self.guests} guests - {self.user.username}"

class BanqueteItem(models.Model):
    banquete = models.ForeignKey(Banquet, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.food.title} for {self.banquete.user.username}"
