from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from tattoo_web.articles.views import is_admin
from tattoo_web.photos.forms import BasePhotoForm
from tattoo_web.photos.models import ArtistPhoto, UserPhoto


class PhotosListView(views.ListView):
    model = ArtistPhoto
    template_name = 'photos/photo_gallery.html'
    context_object_name = 'photos'


class PhotoDetailsView(views.DetailView):
    model = ArtistPhoto
    template_name = 'photos/photo-details-page.html'
    context_object_name = 'photo'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class PhotoAddView(LoginRequiredMixin, views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = BasePhotoForm

    success_url = reverse_lazy('gallery')


@method_decorator(user_passes_test(is_admin), name='dispatch')
class PhotoEditView(LoginRequiredMixin, views.UpdateView):
    model = ArtistPhoto
    template_name = 'photos/photo-edit-page.html'
    form_class = BasePhotoForm

    success_url = reverse_lazy('gallery')


@method_decorator(user_passes_test(is_admin), name='dispatch')
class PhotoDeleteView(LoginRequiredMixin, views.DeleteView):
    model = ArtistPhoto
    template_name = 'photos/photo-delete-page.html'

    success_url = reverse_lazy('gallery')


class UserPhotosListView(views.ListView):
    model = UserPhoto
    template_name = 'photos/user_photo_gallery.html'
    context_object_name = 'user_photos'


class UserPhotoDetailsView(LoginRequiredMixin, views.DetailView):
    model = UserPhoto
    template_name = 'photos/user_photo-details-page.html'
    context_object_name = 'user_photo'


class UserPhotoAddView(LoginRequiredMixin, views.CreateView):
    template_name = 'photos/user_photo-add-page.html'
    form_class = BasePhotoForm

    success_url = reverse_lazy('')


class UserPhotoEditView(LoginRequiredMixin, views.UpdateView):
    model = UserPhoto
    template_name = 'photos/user_photo-edit-page.html'
    form_class = BasePhotoForm

    success_url = reverse_lazy('user gallery')


class UserPhotoDeleteView(LoginRequiredMixin, views.DeleteView):
    model = UserPhoto
    template_name = 'photos/user_photo-delete-page.html'

    success_url = reverse_lazy('user gallery')

