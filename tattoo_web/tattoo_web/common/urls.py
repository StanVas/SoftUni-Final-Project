from django.urls import path

from tattoo_web.common.views import HomeView, photo_like, photo_comment, article_like, article_comment, \
    copy_link_to_clipboard

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('like/<int:photo_id>/', photo_like, name='like photo '),
    path('comment/<int:photo_id>/', photo_comment, name='comment photo '),
    path('like/<int:article_id>/', article_like, name='like article'),
    path('comment/<int:article_id>/', article_comment, name='comment article'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share photo'),
    # article share
)
