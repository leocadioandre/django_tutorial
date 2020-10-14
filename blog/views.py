from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from . models import Post

# Create your views here. Controla as listagem dos dados e as views

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html' #indica o caminho dos templates


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('autor','titulo','conteudo')

""" Poderia indicar no campo fields apenas os campos necessarios, sendo ou todos 
feild = '__all__'
"""
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('titulo', 'conteudo')

