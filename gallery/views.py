from django.http import Http404
from django.views import generic
from django.utils import timezone
from models import Gallery, Image


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.get_published()


class AlbumView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/album.html'
    context_object_name = 'album'
    slug_field = 'slug'

    def get_object(self):
        try:
            gallery = super(AlbumView, self).get_object()
            if gallery.pub_date >= timezone.now():
                raise Gallery.DoesNotExist
        except Gallery.DoesNotExist:
            raise Http404
        return gallery


class ImageView(generic.TemplateView):
    template_name = 'gallery/image.html'

    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        try:
            context['image'] = Image.get_published().get(
                slug=self.kwargs['slug'],
                gallery__slug=self.kwargs['albumslug']
            )
        except Image.DoesNotExist:
            raise Http404

        return context
