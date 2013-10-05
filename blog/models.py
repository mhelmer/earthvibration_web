from django.db import models
from taggit.managers import TaggableManager


class BlogEntry(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField('slug', unique_for_date='date_published')
    date_published = models.DateTimeField('date published')
    date_modified = models.DateTimeField('last modified')
    content = models.TextField()
    author = models.CharField(max_length=100)

    tags = TaggableManager()

    @models.permalink
    def get_absolute_url(self):
        return ('devblog_post_url', (), {
            'year': self.date_published.year,
            'month': self.date_published.month,
            'day': self.date_published.day,
            'slug': self.slug})
