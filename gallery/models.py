from django.core.urlresolvers import reverse
from django.db import models
from sorl.thumbnail import ImageField
import os


def get_image_path(instance, filename):
    return os.path.join('gallery', str(instance.gallery.slug), filename)


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField('slug', unique=True)
    pub_date = models.DateTimeField('date published')
    subtitle = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=150)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField('slug')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)

    gallery = models.ForeignKey(Gallery)
    image = ImageField(upload_to=get_image_path)
    location = models.ForeignKey(Location, blank=True, null=True)
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)
        unique_together = ('slug', 'gallery')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:image',
                       kwargs={'albumslug': self.gallery.slug,
                               'slug': self.slug})

    def get_next(self):
        next = Image.objects.filter(order__gt=self.order)
        if next:
            return next[0]
        return Image.objects.filter(order__lt=self.order)[0]

    def get_prev(self):
        prev = Image.objects.filter(order__lt=self.order).reverse()
        if prev:
            return prev[0]
        return Image.objects.filter(order__gt=self.order).reverse()[0]
