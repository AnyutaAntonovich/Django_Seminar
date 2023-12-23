from django.db import models
from django.utils import timezone


class Coins(models.Model):
    tuple_choice = (('h', 'heads'), ('t', 'tails'))
    values = models.CharField(max_length=1, choices=tuple_choice)
    time = models.DateTimeField(default=timezone.now)

    @staticmethod
    def last_count(count: int):
        last_state = Coins.objects.order_by('-time')[:count]
        dict_ = {'heads': 0, 'tails': 0}
        for i in last_state:
            if i.values == 'h':
                dict_['heads'] += 1
            else:
                dict_['tails'] += 1
        return dict_

# Create your models here.
