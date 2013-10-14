from django.views import generic
from django.utils import timezone

from taggit.models import Tag
from models import BlogEntry


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'published_blog_entries'

    def get_queryset(self):
        """
        Return the published blog entries
        """
        return BlogEntry.objects.filter(
            date_published__lte=timezone.now()
        ).order_by('-date_published')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        blog_entries_dj = BlogEntry.objects.filter(
            attachment_type__model='tune')


        context['players'] = [{'tune': dj_e.attachment_object, 'suffix': dj_e.pk}
                              for dj_e in blog_entries_dj]
        return context


class DetailsView(generic.dates.DateDetailView):
    template_name = 'blog/details.html'
    model = BlogEntry
    date_field = 'date_published'
    context_object_name = 'blog_entry'


class TagView(generic.ListView):
    template_name = 'blog/tag.html'
    context_object_name = 'published_blog_entries'
    #Need to pass tag aswell, somehow

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        """
        Return the published blog entries
        """
        return BlogEntry.objects.filter(
            tags__slug__in=[self.kwargs['slug']]
        ).order_by('-date_published')
