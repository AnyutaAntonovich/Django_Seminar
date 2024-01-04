from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import AddAuthorForm
import logging


logger = logging.getLogger(__name__)


def author(request):
    logger.info('Page accessed')
    author = User.objects.filter(name='Name1')
    print(author)
    context = {'author': author[0]}
    return render(request, 'modelapp/author.html', context=context)



def author_create(request):
    logger.info('Page accessed')
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            age = form.cleaned_data['age']
        # print(name, surname, email, bio, age)
        user = User(name= name, surname= surname, email= email, bio= bio, age= age)
        user.save()
    else:
        form = AddAuthorForm()

    return render(request, 'modelapp/author_create.html', {'form': form})
