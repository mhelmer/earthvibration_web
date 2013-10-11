from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from djplayer.templatetags import djplayer_extras
from djplayer.models import Tune
from blog.models import BlogEntry

register = template.Library()


def get_tag_url(tag):
    return reverse('blog:tags', kwargs={'slug': tag.slug})


def list_tags(blog_entry):
    return {'tags': blog_entry.tags.all()}


def show_blog_entry(blog_entry):
    return {'blog_entry': blog_entry}


def script_attached_js(blog_entries):
    """
    templatetag to include the necessary javascript for all blog entries
    """
    try:
        blog_entries_dj = blog_entries.filter(attachment_type__model='tune',)
    except AttributeError:
        blog_entries_dj = BlogEntry.objects.filter(
            attachment_object_id=blog_entries.attachment_object.pk,
            attachment_type__model='tune')

    tunes = Tune.objects.filter(pk__in=blog_entries_dj)

    r = ''
    if tunes is not None:
        r += djplayer_extras.djwidget_js_base()
        for tune in tunes:
            r += render_to_string('djplayer/djplayer_script.html',
                                  {'tune': tune}
                                  )
    return r


def show_attached_content(blog_entry):
    """
    We want to be able to attach content like media and events to blog
    entries. Template tag should output these attachments.
    """
    if blog_entry.attachment_type.model == 'event':
        t = template.loader.get_template('blog/show_attachment_event.html')
        return t.render(template.Context({
            'event': blog_entry.attachment_object}))
    elif blog_entry.attachment_type.model == 'tune':
        t = template.loader.get_template('blog/show_attachment_tune.html')
        return t.render(template.Context({
            'tune': blog_entry.attachment_object}))
    raise TypeError("Only event and music attachments are supported")


def show_blog_entry_details(blog_entry):
    return {'blog_entry': blog_entry}


register.simple_tag(get_tag_url)
register.inclusion_tag('blog/list_tags.html')(list_tags)
register.inclusion_tag('blog/show_entry.html')(show_blog_entry)
register.inclusion_tag('blog/show_entry_details.html')(
    show_blog_entry_details)

register.simple_tag(show_attached_content)
register.simple_tag(script_attached_js)
