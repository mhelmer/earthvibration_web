from django import template
from django.utils import timezone

register = template.Library()


def list_past_events(events):
    past_events = events.filter(
        date__lte=timezone.now(),
    ).order_by('date')
    return {'events': past_events, 'kind': 'past'}


def list_future_events(events):
    future_events = events.filter(
        date__gte=timezone.now(),
    ).order_by('date')
    return {'events': future_events, 'kind': 'upcoming'}

register.inclusion_tag('events/list_events.html')(list_past_events)
register.inclusion_tag('events/list_events.html')(list_future_events)
