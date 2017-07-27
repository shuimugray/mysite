from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import strip_tags
import markdown
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article(models.Model):
    STATUS_CHOICES=(
        ('d','Draft'),
        ('p','Published'),
    )
    caption = models.CharField('标题',max_length=30)
    subcaption = models.CharField(max_length=50, blank=True)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)
    excerpt=models.CharField(max_length=200,blank=True)
    status=models.CharField('文章状态',max_length=1,choices=STATUS_CHOICES)
    abstract=models.CharField('摘要',max_length=200,blank=True,null=True)
    author = models.CharField(max_length=30)
    category = models.ForeignKey('Category',verbose_name='分类',null=True)
    body = RichTextUploadingField('正文')
    views=models.PositiveIntegerField('浏览量',default=0)
    likes=models.PositiveIntegerField('点赞数',default=0)
    topped=models.BooleanField('置顶',default=False)
    tags=models.ManyToManyField(Tag,blank=True)
    def __str__(self):
        return self.caption
    def get_absolute_url(self):
        return reverse('easyblog:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering=['-created_time']
    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])
    def save(self,*args,**kwargs):
        if not self.excerpt:
            md=markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt=strip_tags(md.convert(self.body))[:54]
        super(Article,self).save(*args,**kwargs)




