from django.urls import include, path

from tattoo_web.articles.views import ArticleDetailsView, ArticleEditView, ArticleDeleteView, ArticleCreateView, \
    ArticlesListView

urlpatterns = (
    path('', ArticlesListView.as_view(), name='articles list'),
    path('create/', ArticleCreateView.as_view(), name='create article'),
    path('<int:pk>/', include([
        path('', ArticleDetailsView.as_view(), name='details article'),
        path('edit/', ArticleEditView.as_view(), name='edit article'),
        path('delete/', ArticleDeleteView.as_view(), name='delete article'),
    ])),
)
