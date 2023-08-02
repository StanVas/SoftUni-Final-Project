from django import forms

from tattoo_web.photos.models import ArtistPhoto, UserPhoto


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = ArtistPhoto
        fields = '__all__'


# We get UserPhoto.user automatically, so we don't need `user` field
class BaseUserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ('photo', 'description',)
