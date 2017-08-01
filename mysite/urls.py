"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from mysite import settings
from easyblog import views
from django.contrib.staticfiles.urls import static


app_name="easyblog"
admin.autodiscover()
urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),
   url(r'', include('easyblog.urls')),
   url(r'^$', views.index, name='index'),
   url(r'index/$', views.index, name='index'),
   url(r'^index/article/(?P<pk>\d+)/$', views.detail, name='detail'),
   url(r'^article/comments/',include('django_comments.urls')),
   url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
   url(r'contact/$', views.contact, name='contact'),
   url(r'^ckeditor/', include('ckeditor_uploader.urls')),
   ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
