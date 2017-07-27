from django.conf.urls import include,url
from django.contrib import admin

from mysite import settings
from easyblog import views
from django.contrib.staticfiles.urls import static

app_name="easyblog"
urlpatterns=[
          url(r'^admin/', include(admin.site.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)