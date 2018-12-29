# blog/models.py
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        """This improves readability inside admin panel"""
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
