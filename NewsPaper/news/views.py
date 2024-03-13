from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.post import Post


class NewsList(ListView):
    model = Post
    ordering = 'post_time_creation'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'