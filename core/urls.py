from django.contrib import admin
from django.urls import path
import core.views

from django.shortcuts import render

urlpatterns = [
    path('', core.views.hello),
]