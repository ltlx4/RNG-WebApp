from django import forms
from random import randint

class GuessForm(forms.Form):
    human_guess = forms.IntegerField(label='Choose a number between 1-20', widget=forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}))


    
