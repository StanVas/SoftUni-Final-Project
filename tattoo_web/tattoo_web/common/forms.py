from django import forms

from tattoo_web.common.models import ArtistPhotoComment, UserPhotoComment


class ArtistPhotoCommentForm(forms.ModelForm):
    class Meta:
        model = ArtistPhotoComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 4,
                    'placeholder': 'Add a comment...',
                },
            ),
        }


class UserPhotoCommentForm(forms.ModelForm):
    class Meta:
        model = UserPhotoComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 4,
                    'placeholder': 'Add a comment...',
                },
            ),
        }
