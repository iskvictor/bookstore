from django.shortcuts import render
from django.http import JsonResponse
from . models import ProductInBasket,ProductInOrder,Order
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)

    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    is_delete=data.get("is_delete")
    print('is_delete',is_delete)
    if is_delete =='true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product,created = ProductInBasket.objects.get_or_create(session_key=session_key,book_id=product_id,is_active=True, defaults={'number':nmb})
        if not created:
            print('created',new_product.number)
            new_product.number += int(nmb)
            new_product.save(force_update=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict['products_total_nmb'] = products_total_nmb

    return_dict['products']=list()
    for item in products_in_basket:
        product_dict = {}
        product_dict['name'] = item.book.name
        product_dict['id'] = item.id
        product_dict['price_per_item'] = item.price_per_item
        product_dict['number'] = item.number
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    form = CheckoutContactForm(request.POST)
    if request.POST:
        print('request.POST', request.POST)
        if form.is_valid():
            print('yes valid')
            data = request.POST
            name = data.get('name')
            phone = data.get('phone')
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id =1)
            print('order',order.id)
            for key, value in data.items():
                if key.startswith('product_in_basket'):
                    product_in_basket_id = key.split('product_in_basket_')[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.number = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(book=product_in_basket.book, number=product_in_basket.number,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

        else:
            print('no valid')
    return render(request, 'orders/checkout.html', locals())