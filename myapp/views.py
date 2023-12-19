import logging
import random

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page accessed')
    return HttpResponse("Hello, world!")


def heads_tails(request):
    logger.info('Page accessed')
    options = ['heads', 'tails']
    choice = random.choice(options)
    return HttpResponse(choice)


def edges(request):
    logger.info('Page accessed')
    edge = random.randint(1, 6)
    return HttpResponse(edge)


def random_num(request):
    logger.info('Page accessed')
    num = random.randint(0, 100)
    return HttpResponse(num)
