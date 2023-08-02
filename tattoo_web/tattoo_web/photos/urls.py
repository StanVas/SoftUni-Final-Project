from django.urls import path, include

from tattoo_web.photos.views import PhotoAddView, PhotoDetailsView, PhotoEditView, PhotoDeleteView, PhotosListView, \
    UserPhotosListView, UserPhotoDetailsView, UserPhotoEditView, UserPhotoDeleteView

urlpatterns = (
    path('', PhotosListView.as_view(), name='gallery'),
    path('add/', PhotoAddView.as_view(), name='add photo'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='details photo'),
        path('edit/', PhotoEditView.as_view(), name='edit photo'),
        path('delete/', PhotoDeleteView.as_view(), name='delete photo'),
    ])),
    # path('user_gallery/', UserPhotosListView.as_view(), name='user_gallery'),
    path('user_gallery/', include([
        path('', UserPhotosListView.as_view(), name='user gallery'),
        path('<int:pk>/', include([
            path('details/', UserPhotoDetailsView.as_view(), name='details user photo'),
            path('edit/', UserPhotoEditView.as_view(), name='edit user photo'),
            path('delete/', UserPhotoDeleteView.as_view(), name='delete user photo'),
        ])),
    ])),
)
