from django import template

register = template.Library()


def djplayer_widget(tune, suffix=''):
    return {'tune': tune,
            'suffix': suffix}


def djwidget_script_tune(tune, suffix=''):
    players = [{'tune': tune, 'suffix': suffix}]
    return {'players': players}


def djwidget_script_tunes(tunes, suffix=''):
    players = [{'tune': tune, 'suffix': suffix} for tune in tunes]
    return {'players': players}


def djwidget_js_players(players):
    return {'players': players}


def djwidget_js_base():
    return '<script type="text/javascript" ' \
           'src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/' \
           'jquery.min.js"></script> \
           <script type="text/javascript" ' \
           'src="/static/djplayer/js/jquery.jplayer.min.js"></script>'


def djwidget_js_playlist(tunes, suffix=''):
    return {'tunes': tunes, 'suffix': suffix}


def djwidget_playlist(suffix=''):
    return {'suffix': suffix}


def djwidget_link_css():
    return

register.inclusion_tag('djplayer/djplayer_widget.html')(djplayer_widget)
register.inclusion_tag('djplayer/djplayer_script.html')(djwidget_script_tune)
register.inclusion_tag('djplayer/djplayer_script.html')(
    djwidget_script_tunes)
register.inclusion_tag('djplayer/djplayer_script.html')(
    djwidget_js_players)
register.simple_tag(djwidget_js_base)
register.inclusion_tag('djplayer/djplayer_link_css.html')(djwidget_link_css)

register.inclusion_tag('djplayer/djplayer_pl_js.html')(djwidget_js_playlist)
register.inclusion_tag('djplayer/djplayer_pl.html')(djwidget_playlist)
