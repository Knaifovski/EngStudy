# Copyright © 2022 NickolaQ Knaifovski. All rights reserved.

from django.shortcuts import render, redirect
from .forms import *
from .models import Word
import random
import time
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
from requests import request

def play(request):
    error=""
    form = SimpleForm()
    template_name = 'engcards/play.html'
    AllWords = list(Word.objects.all())
    if request.method == 'POST':
        counter = int(request.POST.get('answer').split(',')[2])
        answer = request.POST.get('answer').split(',')[1]
        word = request.POST.get('answer').split(',')[0]
        print(Word.objects.get(trans=answer), word)
        if word == str(Word.objects.get(trans=answer)):
            print('YES')
            WordRandom = random.choice(AllWords)
            answers=get_answers(WordRandom,5)
            counter+=1
        else:
            print('NO')
            WordRandom=Word.objects.get(word=word)
            error = "{} не перевод слова {}".format(answer,WordRandom)
            answers=get_answers(WordRandom,5)
            counter=0
        time.sleep(0.4)
        data = {'form': form, 'WordRandom': WordRandom, 'answers': answers, 'ERROR': error,'counter':counter}
        return render(request, template_name, data)
    else:
        counter = 0
        WordRandom = random.choice(AllWords)
        answers=get_answers(WordRandom,5)
        data = {'form': form, 'WordRandom': WordRandom, 'answers': answers, 'ERROR': error,'counter':counter}
        return render(request, template_name, data)

def get_answers(word,count:int):
    answers=[]
    i=0
    while i< count:
        answers.append(random.choice(list(Word.objects.all())).trans)
        i+=1
    answers.append(word.trans)
    random.shuffle(answers)
    return answers

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
