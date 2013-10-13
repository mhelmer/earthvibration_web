from django.views import generic
from django.utils import timezone

from models import StudioMediaEntry
from djplayer.models import Tune


class IndexView(generic.TemplateView):
    template_name = "home/home.html"


class SoundsystemView(generic.TemplateView):
    template_name = "home/soundsystem.html"


class StudioView(generic.TemplateView):
    template_name = "home/studio.html"

    def get_context_data(self, **kwargs):
        context = super(StudioView, self).get_context_data(**kwargs)

        media_entries = StudioMediaEntry.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')
        media_tunes = Tune.objects.filter(pk__in=media_entries)
        context['media_tunes'] = media_tunes

        return context


class ReleasesView(generic.TemplateView):
    template_name = "home/releases.html"


class MediaView(generic.TemplateView):
    template_name = "home/media.html"


class EventsView(generic.TemplateView):
    template_name = "home/events.html"


class ContactView(generic.TemplateView):
    template_name = "home/contact.html"
