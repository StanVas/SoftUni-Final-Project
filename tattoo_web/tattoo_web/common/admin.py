from django.contrib import admin

from tattoo_web.common.models import ArtistPhotoComment, UserPhotoComment


@admin.register(ArtistPhotoComment)
class ArtistPhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'date_time_of_publication')
    ordering = ('id',)
    fields = ('user', 'date_time_of_publication', 'text', 'photo',)
    readonly_fields = ('user', 'date_time_of_publication', 'photo',)

@admin.register(UserPhotoComment)
class UserPhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'date_time_of_publication')
    ordering = ('id',)
    fields = ('user', 'date_time_of_publication', 'text', 'photo',)
    readonly_fields = ('user', 'date_time_of_publication', 'photo',)
