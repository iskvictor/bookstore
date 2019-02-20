from django.contrib import admin
from . models import *
# Register your models here.

class BookImageInLine(admin.TabularInline):
    model = BookImage

class VisualInLine(admin.TabularInline):
    model = Visual

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active','id']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','id','price','discount', 'category']
    inlines = [BookImageInLine,VisualInLine]



@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    exclude = ('',)


@admin.register(Visual)
class Visual(admin.ModelAdmin):
    list_display = [field.name for field in Visual._meta.get_fields()]


