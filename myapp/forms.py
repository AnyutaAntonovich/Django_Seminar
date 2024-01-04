from django import forms


class GamesForms(forms.Form):
    tuple_games = (('coins', 'Бросить монетку'), ('edges', 'Бросить кубик'), ('number', 'Угадай число'))
    games_extions = forms.ChoiceField(choices=tuple_games)
    count_games = forms.IntegerField(min_value=1, max_value=64)


