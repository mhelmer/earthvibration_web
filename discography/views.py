from django.views import generic
from discography.models import Release


class IndexView(generic.ListView):
    template_name = 'discography/index.html'
    context_object_name = 'releases'

    def get_queryset(self):
        return Release.objects.filter(
            published=True,
        )
