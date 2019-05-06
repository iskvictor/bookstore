from .models import ProductInBasket
from book.models import BookCategory
def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    categories = BookCategory.objects.all()
    return locals()