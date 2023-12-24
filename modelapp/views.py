from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import logging


logger = logging.getLogger(__name__)


def author(request):
    logger.info('Page accessed')
    author = User.objects.filter(name='Name1')
    print(author)
    context = {'author': author[0]}
    return render(request, 'modelapp/author.html', context=context)

# Create your views here.
