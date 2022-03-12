from django.shortcuts import render

from .models import Book, Author, Publisher


def hello(request):
    print(Author.objects.all())
    context = {'books': Book.objects.all(), 'authors': Author.objects.all(), 'publishers': Publisher.objects.all()}
    return render(request, 'core/hello.html', context)
