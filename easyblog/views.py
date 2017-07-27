from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django_comments.forms import CommentForm

from easyblog.models import Article,Category,Tag
import markdown
from django.db.models import Q
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    article_list=Article.objects.all()
    return render(request,'index.html',context={'article_list':article_list})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.increase_views()
    article.body = markdown.markdown(article.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'article': article})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate)
    return render(request, 'index.html', context={'article_list': article_list})


class CategoryView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class TagView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)

def about(request):
    return render(request,"about.html")

def support(request):
    return render(request,"support.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    blog_list=Article.objects.all().order_by('created_time')
    return render(request,"blog.html",{'blog_list':blog_list})




# Create your views here.
