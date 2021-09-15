from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import GuessForm
from django.http import HttpResponse
from django.contrib import messages
from random import randint
# Create your views here.
class Generator(View):
    
    def get(self, request, *args, **kwargs):
        form = GuessForm()
        return render(request, 'rng_generator/form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = GuessForm(request.POST or None)
        if form.is_valid():
            human_guess = form.cleaned_data['human_guess']
            a = randint(0, 1)
            try:
                if a == human_guess:
                    messages.success(request, "Correct Guess!\n The correct answer is:" + str(a))
                    return redirect('index')
                else:
                    messages.error(request, "Wrong Guess!\n The correct answer was:" + str(a))
                    return redirect('index')
            except KeyError:
                messages.error(request, "Not Valid, Try again")
                return render('index')