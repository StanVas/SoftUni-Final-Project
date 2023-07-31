from django import forms

from tattoo_web.photos.models import ArtistPhoto


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = ArtistPhoto
        fields = '__all__'
