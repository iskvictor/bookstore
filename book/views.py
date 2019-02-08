from django.views.generic import ListView, DetailView
from book.models import Book, BookImage

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        images_books = BookImage.objects.filter(is_active=True, is_main=True,book__is_active=True)
        context['images_books'] = images_books
        context['product_images_superhit'] = images_books.filter(book__category__name='Суперхиты')
        context['product_images_new'] = images_books.filter(book__category__name='Новинки')
        context['product_images_pre_order'] = images_books.filter(book__category__name='Предзаказ')
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.cycle_key()
        print("session_key",session_key)
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book.html"
    context_object_name = "detail_book"