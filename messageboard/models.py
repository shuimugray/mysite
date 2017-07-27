from django.db import models

class MsgPost(models.Model):
    user = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ['-datetime']
# Create your models here.
