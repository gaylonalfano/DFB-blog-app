# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse_lazy
#from django.shortcuts import render


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


'''
On the top two lines we import ListView and our database model Post. Then we
subclass ListView and add links to our model and template. This saves us a lot
of code versus implementing it all from scratch.
'''
