from django.views import generic as views


class ArticleAddView(views.CreateView):
    pass


class ArticleDetailsView(views.DetailView):
    pass


class ArticleEditView(views.UpdateView):
    pass


class ArticleDeleteView(views.DeleteView):
    pass
