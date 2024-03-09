from django.db import models
from django.contrib.auth.models import User
from news.models.post import Post


class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment_text = models.TextField(max_length=500)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
