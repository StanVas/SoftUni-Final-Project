from django.contrib import admin

from tattoo_web.photos.models import ArtistPhoto, UserPhoto


@admin.register(ArtistPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'description',)
    ordering = ('pk',)


@admin.register(UserPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'description',)
    ordering = ('pk',)
