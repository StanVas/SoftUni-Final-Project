from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'common/home.html'


def photo_like(request, photo_id):
    pass


def photo_comment(request, photo_id):
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
