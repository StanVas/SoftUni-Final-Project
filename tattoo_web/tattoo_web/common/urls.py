from django.urls import path

from tattoo_web.common.views import HomeView, photo_like, article_like, article_comment, \
    copy_link_to_clipboard, ArtCommentEditView, ArtCommentDeleteView, UserCommentEditView, UserCommentDeleteView, \
    AboutMeView, ContactsView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about_me/', AboutMeView.as_view(), name='about me'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('art_comment/<int:pk>/edit/', ArtCommentEditView.as_view(), name='edit comment art'),
    path('art_comment/<int:pk>/delete/', ArtCommentDeleteView.as_view(), name='delete comment art'),

    path('user_comment/<int:pk>/edit/', UserCommentEditView.as_view(), name='edit comment user'),
    path('user_comment/<int:pk>/delete/', UserCommentDeleteView.as_view(), name='delete comment user'),

    path('like/<int:photo_id>/', photo_like, name='like photo'),

    path('like/<int:article_id>/', article_like, name='like article'),
    path('comment/<int:article_id>/', article_comment, name='comment article'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share photo'),
    # article share
)
