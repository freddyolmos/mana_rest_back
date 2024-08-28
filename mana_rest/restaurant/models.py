from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def __str__(self):
        return f"{self.title}"
    

class Store(models.Model):
    user = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)

class Ticket(models.Model):
    # Relaciona el ticket con una tienda específica
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='tickets')
    
    # Fecha y hora del ticket
    date = models.DateTimeField(auto_now_add=True)
    
    # Total del ticket
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Estado del ticket (pagado, pendiente, cancelado, etc.)
    STATUS_CHOICES = [
        ('PAG', 'Pagado'),
        ('PEN', 'Pendiente'),
        ('CAN', 'Cancelado'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    
    # Nombre del cliente
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Comidas asociadas al ticket
    foods = models.ManyToManyField(Food, through='TicketItem')

    def __str__(self):
        return f"Ticket #{self.id} - {self.store} - {self.get_status_display()}"

class TicketItem(models.Model):
    # Relaciona un ítem con un ticket específico
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    
    # Relaciona un ítem con una comida específica
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    
    # Cantidad de la comida en el ticket
    quantity = models.PositiveIntegerField(default=1)
    
    # Precio total de este ítem específico
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.food.title} - Ticket #{self.ticket.id}"
