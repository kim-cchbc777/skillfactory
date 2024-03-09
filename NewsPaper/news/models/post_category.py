from django.db import models
from news.models.category import Category
from news.models.post import Post


class PostCategory(models.Model):
    posts = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ForeignKey(Post, on_delete=models.CASCADE)
