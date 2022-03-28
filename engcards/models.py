from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=30)
    trans = models.CharField(max_length=30)
    # img = models.ImageField(blank=True)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.word}'
    def get_absolute_url(self):
        return f'/{self.id}'
    def get_answer(self):
        return f'{self.trans}'

    class Meta:
        verbose_name='Word'
        verbose_name_plural='Words'