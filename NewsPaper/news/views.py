from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.post import Post
from pprint import pprint


class NewsList(ListView):
    model = Post
    ordering = '-post_time_creation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # pprint(context)
    #     return context