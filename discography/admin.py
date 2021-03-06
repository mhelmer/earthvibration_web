from django.contrib import admin
from discography.models import Release, Track, Artist, CoverImage, RelFormat
from sorl.thumbnail.admin import AdminImageMixin


class TrackInline(admin.TabularInline):
    model = Track
    extra = 0


class CoverImageInline(AdminImageMixin, admin.TabularInline):
    model = CoverImage
    extra = 0


class ReleaseAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':
                         ['title', 'slug', 'release_date', 'catalog_number',
                          'rel_format', 'published', 'tune', 'label']})
                 ]
    inlines = [TrackInline, CoverImageInline]
    date_hierachy = 'release_date'
    prepopulated_fields = {"slug": ("title",)}


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':
                         ['name', 'slug', 'nationality']})
                 ]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Release, ReleaseAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(RelFormat)
