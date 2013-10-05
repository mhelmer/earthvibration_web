from django.views import generic
from django.utils import timezone

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
