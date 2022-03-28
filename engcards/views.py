# Copyright © 2022 NickolaQ Knaifovski. All rights reserved.

from django.shortcuts import render, redirect
from .forms import *
from .models import Word
import random
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
from requests import request

def play(request):
    start=0
    error="no error"
    form = SimpleForm()
    template_name = 'engcards/play.html'
    print(start)
    AllWords = list(Word.objects.all())
    answers=''
    if request.method == 'POST':
        answer = request.POST.get('answer').split(',')[1]
        word = request.POST.get('answer').split(',')[0]
        print(Word.objects.get(trans=answer), word)
        if word == str(Word.objects.get(trans=answer)):
            print('YES')
            WordRandom = random.choice(AllWords)
            answers = [WordRandom.trans, random.choice(AllWords).trans, random.choice(AllWords).trans]
            random.shuffle(answers)
            # data = {'form': form, 'WordRandom': WordRandom, 'answers': answers, 'ERROR': error}
        else:
            print('NO')
            error = "Nepravilno"
            WordRandom=Word.objects.get(word=word)
            answers = [Word.objects.get(word=word).trans, random.choice(AllWords).trans, random.choice(AllWords).trans]
            random.shuffle(answers)
        data = {'form': form, 'WordRandom': WordRandom, 'answers': answers, 'ERROR': error}
        return render(request, template_name, data)
    else:
        WordRandom = random.choice(AllWords)
        answers = [WordRandom.trans, random.choice(AllWords).trans, random.choice(AllWords).trans]
        random.shuffle(answers)
        # form.reload()
        data = {'form': form, 'WordRandom': WordRandom, 'answers': answers, 'ERROR': error}
        return render(request, template_name, data)

# class WordPlay(DetailView):
#     model = Word
#     template_name = 'engcards/play.html'
#     form_class = WordForm

def add(request):
    error = ''
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Form invalid'
    form = WordForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'engcards/add.html', data)


def main(request):
    return render(request, 'engcards/main.html')
