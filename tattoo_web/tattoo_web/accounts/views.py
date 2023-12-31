from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from tattoo_web.accounts.forms import RegisterUserForm, EditUserForm
from tattoo_web.common.models import UserReview, ArtistPhotoComment, UserPhotoComment

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm

    success_url = reverse_lazy('home')

    # auto login after registration
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object

        login(self.request, user)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        return super().form_valid(form)


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        user_id = self.kwargs['pk']
        context['reviews'] = UserReview.objects.filter(user_id=user_id)
        context['art_comments'] = ArtistPhotoComment.objects.filter(user_id=user_id)
        context['user_comments'] = UserPhotoComment.objects.filter(user_id=user_id)

        return context


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit-page.html'

    form_class = EditUserForm

    # success_url = reverse_lazy('home')

    context_object_name = 'profile'

    def get_success_url(self):
        return reverse('details user', kwargs={'pk': self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     return context


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'

    success_url = reverse_lazy('home')

    context_object_name = 'profile'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     return context
