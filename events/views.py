from django.views import generic
from models import Event


class IndexView(generic.TemplateView):
    template_name = 'events/index.html'


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
