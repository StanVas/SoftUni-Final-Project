from django.contrib import admin

from tattoo_web.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'sub_title',)
    ordering = ('pk',)
    search_fields = ['title']
    fieldsets = (
        ('Titles', {'fields': ('title', 'sub_title',)}),
        ('Images', {'fields': ('main_image', 'secondary_image', 'extra_image',)}),
        ('Text Content', {'fields': ('byline', 'main_text', 'conclusion',)}),
    )
