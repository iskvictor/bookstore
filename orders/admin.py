from django.contrib import admin
from . models import *

# Register your models here.
class ProductInOrderInLine(admin.TabularInline):
    model = ProductInOrder


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    exclude = ('',)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [ProductInOrderInLine]


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    exclude = ('',)

@admin.register(ProductInBasket)
class ProductInBasketrAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.get_fields()]




