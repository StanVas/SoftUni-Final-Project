from django.urls import path, include

from tattoo_web.photos.views import PhotoAddView, PhotoDetailsView, PhotoEditView, PhotoDeleteView

urlpatterns = (
    path('add/', PhotoAddView.as_view(), name='add photo'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='details photo'),
        path('edit/', PhotoEditView.as_view(), name='edit photo'),
        path('delete/', PhotoDeleteView.as_view(), name='delete photo'),
    ])),
)
