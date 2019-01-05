from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    thumb = models.ImageField(default='idefault.png', blank=True, null=True)
    author = models.ForeignKey(User, blank=False, default=None, on_delete=models.CASCADE)

    # add in author later


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'



