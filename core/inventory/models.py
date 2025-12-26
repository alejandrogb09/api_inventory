from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Movement(models.Model):
    ENTRY = 'IN'
    EXIT = 'OUT'

    MOVEMENT_TYPES = [
        (ENTRY, 'Entrada'),
        (EXIT, 'Salida'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)