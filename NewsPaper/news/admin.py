from django.contrib import admin
from .models.author import Author
from .models.post import Post
from .models.category import Category
from .models.post_category import PostCategory
from .models.comment import Comment

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
