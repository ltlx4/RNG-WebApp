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
        msg = request.session.get('msg', False)
        if (msg): del(request.session['msg'])
        form = GuessForm()
        return render(request, 'rng_generator/form.html', {'form': form, 'message': msg})

    def post(self, request, *args, **kwargs):
        form = GuessForm(request.POST or None)
        if form.is_valid():
            human_guess = form.cleaned_data['human_guess']
            # a = randint(0, 20)
            a = 0
            if human_guess > 20 or human_guess < 0:
                messages.error(request, "Input out of range. Try numbers between 0 and 20.")
                return redirect(request.path)

            if a == human_guess:
                messages.info(request, "Great Guess!\n The correct answer was:" + str(a))
                return redirect(request.path)
            else:
                messages.error(request, "Wrong Guess!\n The correct answer was:" + str(a))
                return redirect(request.path)
