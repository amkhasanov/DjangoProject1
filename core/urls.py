from django.contrib import admin
from django.urls import path
import core.views

from django.shortcuts import render

urlpatterns = [
    path('', core.views.IndexView.as_view()),
    path('books', core.views.BooksView.as_view()),
    path('books/<int:pk>', core.views.BookDetail.as_view()),

]