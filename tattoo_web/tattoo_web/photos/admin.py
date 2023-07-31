from django.contrib import admin

from tattoo_web.photos.models import ArtistPhoto


@admin.register(ArtistPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'description',)
