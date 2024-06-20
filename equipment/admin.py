from django.contrib import admin
from .models import Workshop, Product, Equipment, EquipmentUsage

admin.site.register(Workshop)
admin.site.register(Product)
admin.site.register(Equipment)
admin.site.register(EquipmentUsage)
