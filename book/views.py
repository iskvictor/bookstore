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
        context['product_images_superhit'] = images_books.filter(book__category__name='Суперхиты')
        context['product_images_new'] = images_books.filter(book__category__name='Новинки')
        context['product_images_pre_order'] = images_books.filter(book__category__name='Предзаказ')
        context['images_for_slider']= Visual.objects.filter(is_active=True)
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.cycle_key()
        print("session_key", session_key)
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
    paginate_by = 28

    def get_context_data(self, **kwargs):
        print('************************************')
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        contacts = BookImage.objects.filter(book__category__slug=self.kwargs['category_slug'],
                                 is_active=True, is_main=True, book__is_active=True)
        context['category']= BookCategory.objects.get(slug=self.kwargs['category_slug']),
        paginator = Paginator(contacts, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['contacts']=file_exams


        return context

