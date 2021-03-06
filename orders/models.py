from django.db import models
from book.models import Book
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True,null=True, default=None)
    is_active = models.BooleanField(default=True)
    comments = models.CharField(max_length=64,blank=True, null=True, default=None)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Статус {}'.format(self.name)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статутсы заказов'


class Order(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, null=True)#total price in order
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    address = models.CharField(max_length= 128, blank=True, null=True, default=None)
    buying_type = models.CharField(max_length=40,choices=(('Самовывоз','Самовывоз'),('Доставка','Доставка')),default='Самовывоз')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=64, blank=True, null=True, default=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ {},{}'.format(self.id, self.status)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True,null=True, default=None,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, default=None,on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=7, decimal_places=2, default=None)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=None)#number*price
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.book.name)

    class Meta:
        verbose_name = 'Книга в заказе'
        verbose_name_plural = 'Книги  в заказе'

    def save(self, *args, **kwargs):
        if self.book is not None:
            price_per_item = self.book.price
            self.price_per_item = price_per_item
            self.total_price = int(self.number) * price_per_item
            super(ProductInOrder, self).save(*args, **kwargs)
        else:
            print('///none///')

def product_in_order_post_save(sender, instance, **kwargs):
    order = instance.order
    all_book_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_book_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128,blank=True,null=True, default=None)
    order = models.ForeignKey(Order, blank=True,null=True, default=None,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, default=None,on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0 )#number*price
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.book)


    class Meta:
        verbose_name = 'Книга в корзине'
        verbose_name_plural = 'Книги  в корзине'


    def save(self, *args, **kwargs):
        price_per_item = self.book.price
        self.price_per_item = price_per_item
        self.total_price = int(self.number) * price_per_item
        super(ProductInBasket, self).save(*args, **kwargs)


















