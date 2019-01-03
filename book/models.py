from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=64,blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' {}'.format(self.name)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class BookImage(models.Model):
    book = models.ForeignKey(Book,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' {}'.format(self.id)

    class Meta:
        verbose_name = 'Фотография книги'
        verbose_name_plural = 'Фотографии книг'