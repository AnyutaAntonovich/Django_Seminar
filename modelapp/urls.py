from django.contrib import admin
from django.urls import path, include

from .views import author, author_create

urlpatterns = [
    path('author/', author, name='author'),
    path('create/', author_create, name='author create'),
    ]
