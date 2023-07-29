from django.views import generic as views


class PhotoAddView(views.CreateView):
    pass


class PhotoDetailsView(views.DetailView):
    pass


class PhotoEditView(views.DetailView):
    pass


class PhotoDeleteView(views.DetailView):
    pass
