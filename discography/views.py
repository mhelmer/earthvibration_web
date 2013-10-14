from django.http import Http404
from django.views import generic
from discography.models import Release


class IndexView(generic.ListView):
    template_name = 'discography/index.html'
    context_object_name = 'releases'

    def get_queryset(self):
        return Release.objects.filter(
            published=True,
        ).order_by('-release_date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['players'] = [rel.tune
                              for rel in self.get_queryset()]
        return context


class ReleaseView(generic.TemplateView):
    model = Release
    template_name = 'discography/release.html'
    context_object_name = 'release'
    date_field = 'release_date'

    def get_context_data(self, **kwargs):
        context = super(ReleaseView, self).get_context_data(**kwargs)

        try:
            release = Release.objects.get(
                slug=self.kwargs['slug'],
                release_date__year=self.kwargs['year']
            )
        except Release.DoesNotExist:
            raise Http404

        context['release'] = release
        return context
