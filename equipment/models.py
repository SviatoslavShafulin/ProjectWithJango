from django.db import models

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class EquipmentUsage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    usage_date = models.DateField()
    hours_used = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.equipment.name}"
