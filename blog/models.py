from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

from likes.models import Like


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
