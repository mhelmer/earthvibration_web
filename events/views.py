from django.views import generic
from models import Event


class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'published_events_list'

    def get_queryset(self):
        """
        Return the published events
        """
        return Event.objects.filter(
            published=True
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
