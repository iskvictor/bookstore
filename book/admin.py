from django.contrib import admin
from . models import *
# Register your models here.

class BookImageInLine(admin.TabularInline):
    model = BookImage


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','id','price']
    inlines = [ BookImageInLine ]


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    exclude = ('',)


