from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    # second_name = models.CharField(max_length=55, blank=True)
    # last_name = models.CharField(max_length=55)
    # email = models.EmailField(unique=True)
    # bio = models.TextField(blank=True)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = sum(post.post_rating * 3 for post in self.posts.all())
        comment_rating = sum(comment.comment_rating for comment in self.user.user_comments.all())
        comment_post_rating = sum(comment.comment_rating for post in self.posts.all() for comment in post.post_comments.all())

        self.author_rating = posts_rating + comment_rating + comment_post_rating
        self.save()