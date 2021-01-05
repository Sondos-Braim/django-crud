from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie

# Create your views here.
class movies_view(ListView):
    template_name='home.html'
    model=Movie

class details_view(DetailView):
    template_name='details.html'
    model=Movie

class add_view(CreateView):
    template_name='add.html'
    model=Movie
    fields=['title','director','rate','description']

class update_view(UpdateView):
    template_name='update.html'
    model=Movie
    fields=['title','director','rate','description']

class delete_view(DeleteView):
    template_name='delete.html'
    model=Movie
    fields=['title','director','rate','description']
    success_url = reverse_lazy('home')
