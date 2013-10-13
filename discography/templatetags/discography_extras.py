from django import template
from django.template.loader import render_to_string

register = template.Library()


def script_attached_js(releases, suffix):
    """
    templatetag to include the necessary javascript for all listed releases
    """

    r = ''
    players = [{'tune': rel.tune, 'suffix': suffix} for rel in releases]
    if players is not None:
        r += render_to_string('djplayer/djplayer_script.html',
                              {'players': players})
    return r

register.simple_tag(script_attached_js)
