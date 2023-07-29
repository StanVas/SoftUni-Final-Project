from django.urls import path, include

from tattoo_web.accounts.views import LoginUserView, LogoutUserView, RegisterUserView, ProfileDetailsView, \
    ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details user'),
        path('edit/', ProfileEditView.as_view(), name='edit user'),
        path('delete/', ProfileDeleteView.as_view(), name='delete user'),
    ])),
)
