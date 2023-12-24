from django.contrib import admin
from django.urls import path, include

from .views import author

urlpatterns = [
    path('author/', author, name='author'),
    ]
