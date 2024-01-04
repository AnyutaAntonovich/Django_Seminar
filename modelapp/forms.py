from django import forms
from .models import User


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'bio', 'age']

