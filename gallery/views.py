from django.http import Http404
from django.views import generic
from django.utils import timezone
from models import Gallery, Image


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.filter(
            pub_date__lte=timezone.now(),
        )


class ImageView(generic.TemplateView):
    template_name = 'gallery/image.html'

    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        try:
            context['image'] = Image.objects.get(
                slug=self.kwargs['slug'],
                gallery__slug=self.kwargs['galleryslug']
            )
        except Image.DoesNotExist:
            raise Http404

        return context
