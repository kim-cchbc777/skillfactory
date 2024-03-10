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
com_5 = Comment.objects.create(posts=post_2,comment_text='Some text',autor=user_4)
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

# Обновить рейтинги пользователей.

author_1.update_rating()
author_2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

top_author = Author.objects.order_by('-author_rating').first()
print(f"Username: {top_author.user.username}, Rating: {top_author.author_rating}")

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

post_1.post_title = 'Post Title 1' #  Добавим заголовок к статьям контент
post_1.save()
post_1.post_content = 'Находящийся под домашним арестом в Дубае (ОАЭ) нападающий московского «Спартака» Квинси Промес\
                       поддержал своих одноклубников перед матчем 20-го тура чемпионата России по футболу с воронежским «Факелом»'
post_1.save()

post_2.post_title = 'Post Title 2'
post_2.save()
post_2.post_content = 'Учёный из Перми, кандидат физико-математических наук, доцент кафедры прикладной физики Пермского\
                        Политеха Эргаш Нуруллаев рассказал о влиянии на человека излучения от бытовых приборов'
post_2.save()

news_1.post_title = 'News Title 1'
news_1.save()

news_1.post_content = 'По данным Ассоциации компаний интернет-торговли и Сбербанка, доля трансграничной торговли\
                        сократилась с 36% в 2017 году до всего лишь 3% в 2023 году.Одновременно с этим, объемы интернет-торговли в стране\
                         выросли в шесть раз, достигнув 6,3 триллиона рублей, в сравнении с 1,04 триллиона рублей несколько лет назад. \
                         Это говорит о том, что российские потребители все чаще предпочитают делать покупки внутри страны.'
news_1.save()

best_post = Post.objects.order_by('-post_rating').first()
print(f"Creation Date: {best_post.post_time_creation.strftime('%Y-%m-%d %H:%M:%S')},\n"
      f"Username: {best_post.author.user.username},\n"
      f"Rating: {best_post.post_rating},\n"
      f"Title: {best_post.post_title},\n"
      f"Content: {best_post.preview()}\n")

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
n = 1
for comment in best_post.post_comments.all():
    print(f"Comment Nº {n},\n"
          f"Date: {comment.comment_time},\n"
          f"User: {comment.autor},\n"
          f"Rating: {comment.comment_rating},\n"
          f"Text: {comment.comment_text}\n"
          )

