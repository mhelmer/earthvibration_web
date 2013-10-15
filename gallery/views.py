from django.views import generic
from django.utils import timezone
from models import Gallery


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.filter(
            pub_date__lte=timezone.now(),
        )
