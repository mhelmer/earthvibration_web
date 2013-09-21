from django import template
from django.utils import timezone

from events.models import Event

register = template.Library()


def list_past_events():
    events = Event.objects.filter(
        date__lte=timezone.now(),
        published = True
    ).order_by('date')
    return {'events': events, 'kind': 'past'}


def list_future_events():
    events = Event.objects.filter(
        date__gte=timezone.now(),
        published = True
    ).order_by('date')
    return {'events': events, 'kind': 'upcoming'}

register.inclusion_tag('events/list_events.html')(list_past_events)
register.inclusion_tag('events/list_events.html')(list_future_events)
