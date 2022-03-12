from django.contrib import admin
from django.urls import path
import core.views

from django.shortcuts import render

urlpatterns = [
    path('', core.views.index),
    path('books', core.views.books),
    path('books/<int:id>', core.views.books_detail),

]