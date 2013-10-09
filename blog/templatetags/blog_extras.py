from django import template
from django.core.urlresolvers import reverse

register = template.Library()


def get_tag_url(tag):
    return reverse('blog:tags', kwargs={'slug': tag.slug})


def list_tags(blog_entry):
    return {'tags': blog_entry.tags.all()}


def show_blog_entry(blog_entry):
    return {'blog_entry': blog_entry}


def show_attached_content(blog_entry):
    """
    We want to be able to attach content like media and events to blog
    entries. Template tag should output these attachments.
    """
    raise NotImplementedError, "Attached content has not been implemented yet"
    pass


def show_blog_entry_details(blog_entry):
    return {'blog_entry': blog_entry}


register.simple_tag(get_tag_url)
register.inclusion_tag('blog/list_tags.html')(list_tags)
register.inclusion_tag('blog/show_entry.html')(show_blog_entry)
register.inclusion_tag('blog/show_entry_details.html')(
    show_blog_entry_details)
