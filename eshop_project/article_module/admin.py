from django.contrib import admin
from . import models
from django.http import HttpRequest
from .models import Article

# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','url_title','parent', 'is_active']
    list_editable = ['url_title', 'parent','is_active']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','slug','is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request:HttpRequest, obj:Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
