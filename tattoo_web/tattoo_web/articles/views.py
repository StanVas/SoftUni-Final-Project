from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from tattoo_web.articles.forms import BaseArticleForm, EditArticleForm
from tattoo_web.articles.models import Article

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin


def is_admin(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)


class ArticlesListView(views.ListView):
    model = Article
    template_name = 'articles/articles-page.html'
    context_object_name = 'articles'


class ArticleDetailsView(views.DetailView):
    model = Article
    template_name = 'articles/article-details-page.html'
    context_object_name = 'article'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArticleCreateView(LoginRequiredMixin, views.CreateView):
    template_name = 'articles/article-create-page.html'

    form_class = BaseArticleForm

    success_url = reverse_lazy('articles list')


@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArticleEditView(LoginRequiredMixin, views.UpdateView):
    model = Article
    template_name = 'articles/article-edit-page.html'

    form_class = EditArticleForm

    success_url = reverse_lazy('articles list')


@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArticleDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Article
    template_name = 'articles/article-delete-page.html'

    success_url = reverse_lazy('articles list')
