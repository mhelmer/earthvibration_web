from django import template
from discography.models import Release

register = template.Library()


def show_release(release):
    return {'release': release}

def list_releases():
    return {'releases': Release.objects.filter(
            published=True,).order_by('-release_date')}

register.inclusion_tag('discography/show_release.html')(show_release)
register.inclusion_tag('discography/list_releases.html')(list_releases)
