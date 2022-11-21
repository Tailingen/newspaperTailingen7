from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        sum_rating_author = self.post_set.all().aggregate(Sum('rating_post'))['rating_post__sum'] * 3
        sum_rating_comment = self.user.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']
        sum_rating = self.post_set.all().aggregate(Sum('comment__rating_comment'))['comment__rating_comment__sum']
        self.rating = sum_rating_author + sum_rating_comment + sum_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, through = 'SubscribersUsers')

    def __str__(self):
        return self.name

class SubscribersUsers(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    neworart = models.BooleanField(default=False)
    time_in = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislaike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        previewtext = self.text[:123] + '...'
        return previewtext

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislaike(self):
        self.rating_comment -= 1
        self.save()