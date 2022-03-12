from django.shortcuts import render

from .models import Book, Author, Publisher


def index(request):

    return render(request, 'core/index.html')

def books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'core/book_list.html', context)

def books_detail(request, id):
    book = Book.objects.get(id=id)
    context = {'book_title':book.name, 'book_author_name': book.author, 'publisher_name' : book.publisher  }
    return  render(request, 'core/books_detail.html', context )