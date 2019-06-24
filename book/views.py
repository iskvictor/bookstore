from django.views.generic import ListView, DetailView
from book.models import Book, BookImage,BookCategory,Visual
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class BookListView(ListView):
    model = BookImage
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        images_books = BookImage.objects.filter(is_active=True, is_main=True,book__is_active=True)
        context['images_books'] = images_books
        context['product_images_hit'] = images_books.filter(book__category__name='Хиты продаж')
        context['product_images_new'] = images_books.filter(book__category__name='Новинки')
        context['product_images_last_add'] = images_books.filter(book__category__name='Последние поступления')
        context['product_images_sell_it'] = images_books.filter(book__category__name='Раcпродажа')
        context['product_images_recommended_books'] = images_books.filter(book__category__name='Рекомендуемые книги')
        context['images_for_slider']= Visual.objects.filter(is_active=True)
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.cycle_key()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book.html"
    context_object_name = "detail_book"

    def get_object(self):
        return get_object_or_404(Book, slug=self.kwargs['slug'])


class CategoryDetailView(ListView):
    model = BookImage
    template_name = "book/book_category.html"
    paginate_by = 8
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
            context = super(CategoryDetailView, self).get_context_data(**kwargs)
            category = BookCategory.objects.get(slug=self.kwargs['category_slug'])
            context['category'] = category
            return context

    def get_queryset(self):
        return  BookImage.objects.filter(book__category__slug=self.kwargs['category_slug'],
                                         is_active=True, is_main=True, book__is_active=True)