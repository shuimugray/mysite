from django.contrib import admin
from easyblog.models import Article,Category,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['caption','created_time','last_modified_time','category','author']

admin.site.register(Article,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


# Register your models here.
