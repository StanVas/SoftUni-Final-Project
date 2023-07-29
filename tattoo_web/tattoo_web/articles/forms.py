from django import forms

from tattoo_web.articles.models import Article


class BaseArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
