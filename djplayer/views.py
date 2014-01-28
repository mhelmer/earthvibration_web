# Create your views here.
from django.views import generic
from django.http import Http404
from models import Tune


class IndexView(generic.ListView):
    model = Tune
    template_name = 'djplayer/index.html'
    context_object_name = 'tunes'

    def get_queryset(self):
        return Tune.objects.all()


class PlayerView(generic.TemplateView):
    model = Tune
    template_name = 'djplayer/player.html'
    context_object_name = 'tune'
    date_field = 'date_published'

    def get_context_data(self, **kwargs):
        context = super(PlayerView, self).get_context_data(**kwargs)

        try:
            tune = Tune.objects.get(
                slug=self.kwargs['slug'],
                date_published__year=self.kwargs['year']
            )
        except Tune.DoesNotExist:
            raise Http404
        context['tune'] = tune
        return context
