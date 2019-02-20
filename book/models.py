from django.db import models
from django.db.models.signals import pre_save
from transliterate import translit
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=64,blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128,blank=True, null=True, default=None,unique=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('book:list_category', args=[str(self.slug)])

    def __str__(self):
        return ' {}'.format(self.name)

    class Meta:
        verbose_name = 'Категория книги'
        verbose_name_plural = 'Категория книг'

def pre_save_category_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=BookCategory)



class Book(models.Model):
    name = models.CharField(max_length=128,blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128,blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(BookCategory, blank=True, null=True, default=None,on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):

        return ' {}'.format(self.name)



    def get_absolute_url(self):
        return reverse('book:book-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


def pre_save_book_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_book_slug, sender=Book)

class BookImage(models.Model):
    book = models.ForeignKey(Book,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' {}'.format(self.id)


    def get_absolute_url(self):
        return reverse('book:book-detail', kwargs={'slug': self.book.slug})




    class Meta:
        verbose_name = 'Фотография книги'
        verbose_name_plural = 'Фотографии книг'


class Visual(models.Model):
    book = models.ForeignKey(Book,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='visual/')
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' {}'.format(self.id)

    # def get_absolute_url(self):
    #     return reverse('book-detail', kwargs={'slug': self.book.slug})

    class Meta:
        verbose_name = 'Картинка слайдера'
        verbose_name_plural = 'Картинки слайдера'

