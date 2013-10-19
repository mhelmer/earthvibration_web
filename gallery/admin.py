from django.contrib import admin
from django import forms
from django.conf import settings

from models import Gallery, Image
from sorl.thumbnail.admin import AdminImageMixin


class GalleryForm(forms.ModelForm):
    model = Gallery
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = (
            #'http://code.jquery.com/jquery-latest.min.js',
            #'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
            #settings.STATIC_URL + 'gallery/js/menu-sort.js',
            #settings.STATIC_URL + 'js/collapse-inline.js',
        )


class ImageInline(AdminImageMixin, admin.StackedInline):
    fieldsets = [
        (None, {'fields':
                ['title', 'slug', 'subtitle', 'location', 'image', 'order'],
                }),
    ]
    model = Image
    prepopulated_fields = {"slug": ("title",)}
    extra = 0


admin.site.register(Gallery,
                    inlines=[ImageInline],
                    form=GalleryForm,
                    )
