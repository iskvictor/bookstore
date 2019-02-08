from django.contrib import admin
from . models import *
# Register your models here.

class BookImageInLine(admin.TabularInline):
    model = BookImage


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active','id']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','id','price','discount', 'category']
    inlines = [BookImageInLine]


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    exclude = ('',)


