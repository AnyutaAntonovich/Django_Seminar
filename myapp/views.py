import logging
import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Coins
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page accessed')
    name = 'Study Portal'
    adress = 'Kamzina 85'
    context = {'name': name, 'adress': adress}
    return render(request, 'myapp/index.html', context=context)


def about_us(request):
    logger.info('Page accessed')
    name = 'Study Portal'
    adress = 'Kamzina 85'
    type_ = 'Education'
    context = {'name': name, 'adress': adress, 'type_': type_}
    return render(request, 'myapp/about_us.html', context=context)



# def index(request):
#     logger.info('Page accessed')
#     return HttpResponse("Hello, world!")


def heads_tails(request):
    logger.info('Page accessed')
    options = ['heads', 'tails']
    choice = random.choice(options)
    if choice == 'heads':
        result = 'h'
    else:
        result = 't'
    data = Coins(values=result)
    data.save()
    context = {'result': result, 'choice': choice}
    return render(request, 'myapp/games.html', context=context)


def last_state_(request):
    return HttpResponse(f'{Coins.last_count(5)}')


def edges(request):
    logger.info('Page accessed')
    edge = random.randint(1, 6)
    result = edge
    context = {'result': result, 'choice': edge}
    return render(request, 'myapp/games.html', context=context)


def random_num(request):
    logger.info('Page accessed')
    num = random.randint(0, 100)
    result = num
    context = {'result': result, 'choice': num}
    return render(request, 'myapp/games.html', context=context)
