from django import template

register = template.Library()


def show_gallery(gallery, width):
    return {'gallery': gallery, 'width': width}


def gallery_widget(album):
    return {'album': album}

register.inclusion_tag('gallery/show_gallery.html')(show_gallery)
register.inclusion_tag('gallery/widget.html')(gallery_widget)
