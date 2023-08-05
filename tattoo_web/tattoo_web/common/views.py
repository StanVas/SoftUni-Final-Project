from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from tattoo_web.articles.models import Article
from tattoo_web.common.forms import ArtistPhotoCommentForm, UserPhotoCommentForm
from tattoo_web.common.models import ArtistPhotoComment, UserPhotoComment
from tattoo_web.photos.models import UserPhoto, ArtistPhoto


class HomeView(views.TemplateView):
    template_name = 'common/home.html'

    def get(self, request, *args, **kwargs):
        # Retrieve the last four articles from the database
        latest_articles = Article.objects.all().order_by('-id')[:4]
        latest_images = ArtistPhoto.objects.all().order_by('-id')[:4]
        # Pass the latest articles to the template context
        context = {'latest_articles': latest_articles, 'latest_images': latest_images}

        # Render the template with the context
        return render(request, self.template_name, context)


class AboutMeView(views.TemplateView):
    template_name = 'common/about_me.html'


class ArtistPhotoCommentView(LoginRequiredMixin, views.CreateView):
    model = ArtistPhotoComment
    form_class = ArtistPhotoCommentForm

    template_name = 'photos/photo-details-page.html'

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.photo.pk
        })

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.photo_id = self.kwargs['pk']
        return super().form_valid(form)

    # context_object_name = 'art_comment'


class UserPhotoCommentView(LoginRequiredMixin, views.CreateView):
    model = UserPhotoComment
    form_class = UserPhotoCommentForm

    template_name = 'photos/user_photo-details-page.html'

    def get_success_url(self):
        return reverse('details user photo', kwargs={
            'pk': self.object.photo.pk
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_id = self.kwargs['pk']
        context['photo'] = UserPhoto.objects.get(pk=photo_id)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.photo = self.get_context_data()['photo']  # Set the photo for the comment
        return super().form_valid(form)


def photo_like(request, photo_id):
    pass


def article_like(request, article_id):
    pass


def article_comment(request, article_id):
    pass


# @login_required
def copy_link_to_clipboard(request, photo_id):
    pass


#     # pyperclip.copy()
#     copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))
#
#     return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


class ArtCommentEditView(LoginRequiredMixin, views.UpdateView):
    model = ArtistPhotoComment
    template_name = 'common/edit_comment_form.html'

    form_class = ArtistPhotoCommentForm

    def get_success_url(self):
        return reverse('details photo', kwargs={'pk': self.object.photo.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArtCommentDeleteView(LoginRequiredMixin, views.DeleteView):
    model = ArtistPhotoComment
    template_name = 'common/delete_comment_form.html'

    def get_success_url(self):
        return reverse('details photo', kwargs={'pk': self.object.photo.pk})


class UserCommentEditView(LoginRequiredMixin, views.UpdateView):
    model = UserPhotoComment
    template_name = 'common/user_edit_comment_form.html'

    form_class = UserPhotoCommentForm

    def get_success_url(self):
        return reverse('details user photo', kwargs={'pk': self.object.photo.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserCommentDeleteView(LoginRequiredMixin, views.DeleteView):
    model = UserPhotoComment
    template_name = 'common/user_delete_comment_form.html'

    def get_success_url(self):
        return reverse('details user photo', kwargs={'pk': self.object.photo.pk})
