from django import template

register = template.Library()


def show_release(release):
    return {'release': release}

register.inclusion_tag('discography/show_release.html')(show_release)
