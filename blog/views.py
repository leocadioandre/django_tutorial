from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

# Create your views here. Controla as listagem dos dados e as views

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html' #indica o caminho dos templates


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'custom'