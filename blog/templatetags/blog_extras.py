from django import template
from django.core.urlresolvers import reverse

register = template.Library()


def get_tag_url(tag):
    return reverse('blog:tags', kwargs={'slug': tag.slug})


def list_tags(blog_entry):
    return {'tags': blog_entry.tags.all()}


register.simple_tag(get_tag_url)
register.inclusion_tag('blog/list_tags.html')(list_tags)

