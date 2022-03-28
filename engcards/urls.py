from django.urls import path
from engcards.views import *

urlpatterns = [
    path('',main,name='main'),
    path('play',play,name='play'),
    path('add',add,name='add'),

]
