from django.contrib import admin
from blog.models import BlogEntry


class BlogEntryAdmin (admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'date_published',
                           'date_modified', 'content', 'attachment_type',
                           'attachment_object_id', 'author', 'tags']}),
    ]
    list_display = ('title', 'date_published', 'date_modified', 'slug',
                    'author', 'attachment_type')
    list_filter = ['date_published']
    search_fields = ['title', 'content']
    date_hierachy = 'date_published'
    readonly_fields = ('date_published', 'date_modified',)

    def save_model(self, request, obj, form, change):
        if obj.pk is not None:
            obj.author = request.user
        obj.save()

admin.site.register(BlogEntry, BlogEntryAdmin)
