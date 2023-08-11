from django.contrib import admin

from tattoo_web.photos.models import ArtistPhoto, UserPhoto


@admin.register(ArtistPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'description',)
    ordering = ('pk',)
    readonly_fields = ('date_of_publication',)
    fields = ('date_of_publication', 'photo', 'description',)


@admin.register(UserPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'description',)
    ordering = ('pk',)
    readonly_fields = ('user', 'date_of_publication',)
    fields = ('user', 'date_of_publication', 'photo', 'description',)
