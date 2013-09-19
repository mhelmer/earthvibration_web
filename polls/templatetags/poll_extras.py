from django import template
from django.utils import timezone

from polls.models import Poll

register = template.Library()


def show_results(poll):
    choices = poll.choice_set.all()
    return {'choices': choices}


def show_latest_polls(limit=5):
    polls = Poll.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:limit]
    return {'polls': polls}


register.inclusion_tag('polls/show_results.html')(show_results)
register.inclusion_tag('polls/list_latest_polls.html')(show_latest_polls)
