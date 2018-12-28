# blog/views.py
from django.views.generic import ListView, DetailView
from . models import Post
#from django.shortcuts import render


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


'''
On the top two lines we import ListView and our database model Post. Then we
subclass ListView and add links to our model and template. This saves us a lot
of code versus implementing it all from scratch.
'''
