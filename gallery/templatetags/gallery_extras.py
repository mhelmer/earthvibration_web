from django import template

register = template.Library()


def show_gallery(gallery, width):
    return {'gallery': gallery, 'width': width}

register.inclusion_tag('gallery/show_gallery.html')(show_gallery)
