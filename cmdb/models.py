from django.db import models
from django.contrib import admin
class BlogsPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()
admin.site.register(BlogsPost)
# Create your models here.
