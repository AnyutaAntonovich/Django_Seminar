from django.core.management.base import BaseCommand
from modelapp.models import User


class Command(BaseCommand):
    help = "Create author."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = User(name=f'Name{i}',
                         surname=f'Surname{i}',
                         email=f'mail{i}@mail.ru',
                         bio=f'Biography{i}',
                         age=f'Birthday{i}')
            author.save()
        self.stdout.write('Ok')
