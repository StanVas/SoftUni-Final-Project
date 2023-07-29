from django.urls import include, path

from tattoo_web.articles.views import ArticleAddView, ArticleDetailsView, ArticleEditView, ArticleDeleteView

urlpatterns = (
    path('add/', ArticleAddView.as_view(), name='add article'),
    path('<int:pk>/', include([
        path('', ArticleDetailsView.as_view(), name='details article'),
        path('edit/', ArticleEditView.as_view(), name='edit article'),
        path('delete/', ArticleDeleteView.as_view(), name='delete article'),
    ])),
)
