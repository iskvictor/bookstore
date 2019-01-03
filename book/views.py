from django.views.generic import ListView
from book.models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    queryset = Book.objects.filter(is_active=True)
    context_object_name = 'books'