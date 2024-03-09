from django.contrib.auth.models import User
from news.models.author import Author
from news.models.category import Category
from news.models.post import Post
from news.models.comment import Comment


# Создать двух пользователей (с помощью метода User.objects.create_user('username')).

user_1 = User.objects.create_user('User_1')
user_2 = User.objects.create_user('User_2')

# Создать два объекта модели Author, связанные с пользователями.

author_1 = Author.objects.create(user=user_1)
author_2 = Author.objects.create(user=user_2)

# Добавить 4 категории в модель Category.

cat_1 = Category.objects.create(category_name="Sport")
cat_2 = Category.objects.create(category_name="Economy")
cat_3 = Category.objects.create(category_name="Technology")
cat_4 = Category.objects.create(category_name="Science")

# Добавить 2 статьи и 1 новость.

post_1 = Post.objects.create(author=author_1,choice_field='P')
post_2 = Post.objects.create(author=author_1,choice_field='P')
news_1 = Post.objects.create(author=author_1,choice_field='N')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

post_1.categories.add(cat_1)
post_2.categories.add(cat_4,cat_3)
news_1.categories.add(cat_2)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

user_3 = User.objects.create_user('User_3') # Пользователи для комментариев
user_4 = User.objects.create_user('User_4')

com_1 = Comment.objects.create(posts=post_1,comment_text='Some text',autor=user_3)
com_2 = Comment.objects.create(posts=post_1,comment_text='Some text',autor=user_1)
com_3 = Comment.objects.create(posts=post_2,comment_text='Some text',autor=user_4)
com_4 = Comment.objects.create(posts=news_1,comment_text='Some text',autor=user_2)

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

post_1.like()
post_1.like()
post_1.like()
post_2.like()
post_2.like()
post_2.like()
post_2.like()
news_1.like()
com_1.like()
com_1.like()
com_1.like()
com_1.like()
com_2.like()
com_2.like()
com_3.like()
post_1.dislike()
post_2.dislike()
