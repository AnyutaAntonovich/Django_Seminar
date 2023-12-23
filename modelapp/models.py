from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return f'Fullname: {self.name}, {self.surname}'


# class Coins(models.Model):
#     tuple_choice = (('h', 'heads'), ('t', 'tails'))
#     values = models.CharField(max_length=1, choices=tuple_choice)
#     time = models.DateTimeField(default=timezone.now)




from django.db import models

# Create your models here.
