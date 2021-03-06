from django.views.generic import TemplateView, ListView, DetailView

from .models import Book, Publisher


class IndexView(TemplateView):
    template_name = 'core/index.html'


class BooksView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['object_list']
        return context


class BookDetail(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_title'] = context['object'].name
        context['book_author_name'] = context['object'].author
        context['publisher_name'] = context['object'].publisher
        return context


class Publisher(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = context['object_list']
        return context
