from django import template

register = template.Library()


def djplayer_widget(tune):
    return {'tune': tune}


def djwidget_script_tune(tune):
    return {'tune': tune}


def djwidget_js_base():
    return '<script type="text/javascript" ' \
           'src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/' \
           'jquery.min.js"></script> \
           <script type="text/javascript" ' \
           'src="/static/djplayer/js/jquery.jplayer.min.js"></script>'

register.inclusion_tag('djplayer/djplayer_widget.html')(djplayer_widget)
register.inclusion_tag('djplayer/djplayer_script.html')(djwidget_script_tune)
register.simple_tag(djwidget_js_base)
