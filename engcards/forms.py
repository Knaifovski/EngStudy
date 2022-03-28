from .models import Word
from django import forms
import random
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, ChoiceField, Form


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'trans', 'wins', 'loses']
        widgets = {
            "word": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Word"
            }),
            "trans": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Translate"
            })
        }


class SimpleForm(forms.Form):
    model = Word
    AllWords = list(Word.objects.all())
    WordRandom = random.choice(AllWords)
    Answer1 = Word.get_answer(WordRandom)
    Answer2 = Word.get_answer(random.choice(AllWords))
    Answer3 = Word.get_answer(random.choice(AllWords))
    for step in range(random.randint(3, 7)):
        temp = random.randint(3, 7)
        Answer1 = Answer2
        Answer2=temp
        step + 1
    Choices =[
    (Answer1, Answer1),
    (Answer2, Answer2),
    (Answer3, Answer3),]
    Choices=random.sample(Choices, k=3)
    Answers = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect(
            attrs={'class': 'btn btn-primary'}),
        choices=Choices,
    )
    def reload(self):
        Choices=random.sample(self.Choices, k=3)