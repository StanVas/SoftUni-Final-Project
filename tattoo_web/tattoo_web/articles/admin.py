from django.contrib import admin

from tattoo_web.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'sub_title',)
    ordering = ('pk',)