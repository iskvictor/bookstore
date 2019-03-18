from django.shortcuts import render,reverse
from django.http import JsonResponse, HttpResponseRedirect
from . models import ProductInBasket, ProductInOrder, Order, Status
from .forms import OrderForm
from django.contrib.auth.models import User
# Create your views here.
def basket_adding(request):
    print('///////////////// basket_adding')
    session_key = request.session.session_key
    print('-------request.POST',request.POST)
    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    new_product,created = ProductInBasket.objects.get_or_create(session_key=session_key,book_id=product_id,is_active=True, defaults={'number':nmb})
    if not created:
        print('created',new_product.number)
        new_product.number += int(nmb)
        new_product.save(force_update=True)
    return JsonResponse(Product_in_basket(session_key))


def Product_in_basket(session_key):
    print('********Product_in_basket')
    return_dict = dict()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict['products_total_nmb'] = products_total_nmb
    return_dict['products'] = list()
    for item in products_in_basket:
        product_dict = {}
        product_dict['name'] = item.book.name
        product_dict['id'] = item.id
        product_dict['price_per_item'] = item.price_per_item
        product_dict['number'] = item.number
        return_dict['products'].append(product_dict)
    return return_dict


def basket_count(request):
    session_key = request.session.session_key
    return JsonResponse(Product_in_basket(session_key))


def remove_from_cart_view(request):
    session_key = request.session.session_key
    print('remove cart**********')
    print('-----------request.GET',request.GET.get('product_id'))
    product_id = request.GET.get('product_id')
    ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    return JsonResponse(Product_in_basket(session_key))


# def cart(request):
#     session_key = request.session.session_key
#     print('session_key---checkout',session_key)
#     products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
#     form = CheckoutContactForm(request.POST)
#     if request.POST:
#         print('request.POST', request.POST)
#         if form.is_valid():
#             print('yes valid')
#             data = request.POST
#             name = data.get('name')
#             phone = data.get('phone')
#             user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})
#             order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id =1)
#             print('order',order.id)
#             for key, value in data.items():
#                 if key.startswith('product_in_basket'):
#                     product_in_basket_id = key.split('product_in_basket_')[1]
#                     product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
#                     product_in_basket.number = value
#                     product_in_basket.order = order
#                     product_in_basket.save(force_update=True)
#
#                     ProductInOrder.objects.create(book=product_in_basket.book, number=product_in_basket.number,
#                                                   price_per_item=product_in_basket.price_per_item,
#                                                   total_price=product_in_basket.total_price,
#                                                   order=order)
#
#         else:
#             print('no valid')
#     return render(request, 'orders/cart.html', locals())

def make_order(request):

    session_key = request.session.session_key
    print('session_key---checkout',session_key)

    form = OrderForm(request.POST)
    if request.POST:
        print('request.POST', request.POST)
        if form.is_valid():
            print('yes valid')
            first_name = form.cleaned_data.get('first_name')
            print('first_name',first_name)
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            buying_type = form.cleaned_data.get('buying_type')
            address = form.cleaned_data.get('address')
            comments = form.cleaned_data.get('comments')
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': first_name})
            order = Order.objects.create(user=user, first_name=first_name, phone=phone, status_id =1,
                                         last_name=last_name,buying_type=buying_type,address=address,
                                         comments=comments)
            products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
            for product in products_in_basket:
                product_id = product.id
                value =product.number
                product_in_basket = ProductInBasket.objects.get(id=product_id)
                product_in_basket.number = value
                product_in_basket.order = order
                product_in_basket.save(force_update=True)

                ProductInOrder.objects.create(book=product_in_basket.book, number=product_in_basket.number,
                                              price_per_item=product_in_basket.price_per_item,
                                              total_price=product_in_basket.total_price,
                                              order=order)


            # status  = Status.objects.create(default='новый')
            # new_order = Order()
            # new_order.user = request.user
            # # new_order.save()
            # new_order.first_name = first_name
            # new_order.last_name = last_name
            # new_order.phone = phone
            # new_order.address = address
            # new_order.buying_type = buying_type
            # new_order.comments = comments
            #
            # new_order.save()
            # new_order.total_price = products_in_basket.total_price
            return render(request, 'orders/thank_you.html', locals())


def cart(request):
    session_key = request.session.session_key
    print('session_key---checkout',session_key)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return render(request, 'orders/cart.html', locals())

def change_item_qty(request):
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\.')
    session_key = request.session.session_key
    product_basket_id=request.GET.get('product_basket_id')
    qty=request.GET.get('qty')
    print('++++++product_basket_id',product_basket_id)
    print('++++++qty', qty)
    product_in_basket = ProductInBasket.objects.get(id=int(product_basket_id))
    print('product_in_basket++++++++++',product_in_basket)
    product_in_basket.number = qty
    product_in_basket.save(force_update=True)
    return JsonResponse({'ok' : 'ok'})


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return render(request, 'orders/checkout.html', locals())


def order_create_view(request):
    session_key = request.session.session_key
    print('session_key---checkout', session_key)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    form = OrderForm(request.POST)
    context={
        'form':form
    }
    return render(request,'orders/order.html', context)




