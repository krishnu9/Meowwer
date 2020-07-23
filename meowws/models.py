from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL


class MeowwLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meoww = models.ForeignKey("Meoww", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Meoww(models.Model):
    # id = models.AutoField(primary_key=True)
    # A User can have many tweets
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=MeowwLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.content

    class Meta:
        ordering = ['-id']

    @property
    def is_remeoww(self):
        return self.parent != None
