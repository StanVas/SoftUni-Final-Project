from django.urls import path, include

from tattoo_web.common.views import HomeView, photo_like, \
    copy_link_to_clipboard, ArtCommentDeleteView, ArtCommentEditView, UserCommentEditView, UserCommentDeleteView, \
    AboutMeView, ContactsView, CreateReviewView, EditReviewView, DeleteReviewView, UserReviewsView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about_me/', AboutMeView.as_view(), name='about me'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('reviews/', include([
        path('', UserReviewsView.as_view(), name='reviews'),
        path('create/', CreateReviewView.as_view(), name='create review'),
        path('<int:pk>/', include([
            path('edit/', EditReviewView.as_view(), name='edit review'),
            path('delete/', DeleteReviewView.as_view(), name='delete review'),
        ])),
    ])),

    path('art_comment/<int:pk>/edit/', ArtCommentEditView.as_view(), name='edit comment art'),
    path('art_comment/<int:pk>/delete/', ArtCommentDeleteView.as_view(), name='delete comment art'),

    path('user_comment/<int:pk>/edit/', UserCommentEditView.as_view(), name='edit comment user'),
    path('user_comment/<int:pk>/delete/', UserCommentDeleteView.as_view(), name='delete comment user'),

    path('like/<int:photo_id>/', photo_like, name='like photo'),

    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share photo'),
)
