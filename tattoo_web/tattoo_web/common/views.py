import asyncio

from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from tattoo_web.articles.models import Article
from tattoo_web.common.forms import ArtistPhotoCommentForm, UserPhotoCommentForm, UserReviewForm
from tattoo_web.common.models import ArtistPhotoComment, UserPhotoComment, UserReview
from tattoo_web.photos.models import UserPhoto, ArtistPhoto

UserModel = get_user_model()


class HomeView(views.TemplateView):
    template_name = 'common/home.html'

    def get(self, request, *args, **kwargs):
        # Retrieve the last four articles from the database
        latest_articles = Article.objects.all().order_by('-id')[:4]
        latest_images = ArtistPhoto.objects.all().order_by('-date_of_publication')[:4]
        # Pass the latest articles to the template context
        context = {'latest_articles': latest_articles, 'latest_images': latest_images}

        # Render the template with the context
        return render(request, self.template_name, context)


class AboutMeView(views.TemplateView):
    template_name = 'common/about_me.html'


class ContactsView(views.TemplateView):
    template_name = 'common/contacts.html'


class UserReviewsView(views.TemplateView):
    model = UserReview
    template_name = 'common/user-reviews.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reviews'] = UserReview.objects.all()
    #     context['average_rating'] = UserReview.objects.aggregate(Avg('rating'))['rating__avg']
    #     context['total_reviews'] = UserReview.objects.count()
    #     return context

    @async_to_sync
    async def dispatch(self, request, *args, **kwargs):
        all_reviews = UserReview.objects.all()
        total_reviews = await self.get_total_reviews()
        average_rating = await self.get_average_rating()

        self.async_context_data = {
            'total_reviews': total_reviews,
            'reviews': all_reviews,
            'average_rating': average_rating,
        }

        return super().dispatch(request, *args, **kwargs)

    async def get_total_reviews(self):
        loop = asyncio.get_event_loop()
        total_reviews = await loop.run_in_executor(None, self.calculate_total_reviews)
        return total_reviews

    def calculate_total_reviews(self):
        total_reviews = UserReview.objects.count()
        return total_reviews

    async def get_average_rating(self):
        loop = asyncio.get_event_loop()
        average_rating = await loop.run_in_executor(None, self.calculate_average_rating)
        return average_rating

    def calculate_average_rating(self):
        average_rating = UserReview.objects.aggregate(Avg('rating'))['rating__avg']
        return average_rating

    def get_context_data(self, **kwargs):
        return {
            'total_reviews': self.async_context_data['total_reviews'],
            'reviews': self.async_context_data['reviews'],
            'average_rating': self.async_context_data['average_rating']
        }


class CreateReviewView(LoginRequiredMixin, views.CreateView):
    model = UserReview
    form_class = UserReviewForm

    template_name = 'common/create-review-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    success_url = reverse_lazy('reviews')


class EditReviewView(LoginRequiredMixin, views.UpdateView):
    model = UserReview
    form_class = UserReviewForm

    template_name = 'common/edit-review-form.html'

    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteReviewView(LoginRequiredMixin, views.DeleteView):
    model = UserReview

    template_name = 'common/delete-review-form.html'

    success_url = reverse_lazy('reviews')


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


class ProfileReviewsView(views.ListView):
    model = UserReview
    template_name = 'common/user-profile-reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])

        user_profile = UserModel.objects.get(pk=user.pk)

        context['user_reviews'] = UserReview.objects.filter(user=user).order_by('-id')
        context['user_profile'] = user_profile
        return context


class ProfileCommentsView(views.TemplateView):
    template_name = 'common/user-profile-comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])

        user_profile = UserModel.objects.get(pk=user.pk)

        context['user_comment'] = UserPhotoComment.objects.filter(user=user).order_by('-id')
        context['art_comment'] = ArtistPhotoComment.objects.filter(user=user).order_by('-id')
        context['user_profile'] = user_profile
        return context


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
