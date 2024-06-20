from django.shortcuts import render
from .models import Workshop, Product, Equipment, EquipmentUsage

def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, 'equipment/workshop_list.html', {'workshops': workshops})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'equipment/product_list.html', {'products': products})

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment': equipment})

def equipment_usage_list(request):
    equipment_usage = EquipmentUsage.objects.all()
    return render(request, 'equipment/equipment_usage_list.html', {'equipment_usage': equipment_usage})
