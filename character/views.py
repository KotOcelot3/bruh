from django.shortcuts import render
from django.views.generic import ListView

from .models import Character


class IndexView(ListView):
    model = Character
    template_name = 'index.html'
