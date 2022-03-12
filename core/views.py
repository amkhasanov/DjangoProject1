from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from .models import Book

def hello(request):
    return render(request, 'core/hello.html', {'books' : Book.objects.all()})