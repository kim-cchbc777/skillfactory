from django.db import models
from news.resources import POST_TYPE, POST_CATEGORY
from news.models.author import Author
from news.models.category import Category


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    choice_field = models.CharField(max_length=4, choices=POST_TYPE)
    choice_category = models.CharField(max_length=4, choices=POST_CATEGORY, default='Science')
    post_time_creation = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_content[:124] + str("...")

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_content[:50]}'