from django.urls import path
from . import views

urlpatterns = [
    path('workshops/', views.workshop_list, name='workshop_list'),
    path('products/', views.product_list, name='product_list'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment_usage/', views.equipment_usage_list, name='equipment_usage_list'),
]
