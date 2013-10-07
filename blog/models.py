from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class BlogEntry(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField('slug', unique_for_date='date_published')
    date_published = models.DateTimeField('date published')
    date_modified = models.DateTimeField('last modified')
    content = models.TextField()
    author = models.CharField(max_length=100)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={
            'year': self.date_published.strftime("%Y"),
            'month': self.date_published.strftime("%b").lower(),
            'day': self.date_published.strftime("%d"),
            'slug': self.slug,
        })

    # this should be moved into a template tag instead
    def get_absolute_tag_url(tag):
        return reverse('blog:tags', kwargs={'slug': 'en-tag'})
