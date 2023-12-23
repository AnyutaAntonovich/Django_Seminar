from django.urls import path, include
from .views import index, heads_tails, random_num, edges, last_state_

urlpatterns = [
    path('', index, name='index'),
    path('game1/', heads_tails, name='heads_tails'),
    path('game2/', edges, name='edges'),
    path('game3/', random_num, name='random_num'),
    path('last_state/', last_state_, name='last_state_'),
]
