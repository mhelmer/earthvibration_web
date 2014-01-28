from django.http import Http404
from django.views import generic
from discography.models import Release, Artist


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


class ArtistView(generic.DetailView):
    context_object_name = 'artist'
    template_name = 'discography/artist.html'
    model = Artist
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArtistView, self).get_context_data(**kwargs)

        tracks = context['artist'].track_set.all().values_list(
            'release', flat=True).distinct()
        context['releases'] = Release.objects.filter(
            pk__in=tracks).order_by('release_date')

        return context
