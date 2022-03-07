from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

def hello(request):
    return render(request, 'core/hello.html', {'name':'Vasya'})