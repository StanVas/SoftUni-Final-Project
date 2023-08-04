from django.contrib import admin

from tattoo_web.common.models import ArtistPhotoComment, UserPhotoComment


@admin.register(ArtistPhotoComment)
class ArtistPhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'date_time_of_publication')
    ordering = ('pk',)


@admin.register(UserPhotoComment)
class UserPhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'date_time_of_publication')
    ordering = ('pk',)


# @admin.register(ArticleComment)
# class ArticleCommentAdmin(admin.ModelAdmin):
#     pass
