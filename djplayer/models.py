from django.core.urlresolvers import reverse
from django.db import models
import os

from sorl.thumbnail import ImageField


def get_file_path(instance, filename):
    return os.path.join('audio', str(instance.date_created.year),
                        str(instance.slug), 'mp3', filename)


def get_image_path(instance, filename):
    return os.path.join('audio', str(instance.date_created.year),
                        str(instance.slug), 'AlbumArt.jpg')


class Tune(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField('slug', unique_for_year='date_published')
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_published = models.DateTimeField('date published')
    mp3_file = models.FileField(upload_to=get_file_path)
    album_art = ImageField(upload_to=get_image_path,
                           default='audio/AlbumArt.jpg')

    def get_absolute_url(self):
        return reverse('djplayer:player', kwargs={
            'year': self.date_published.strftime("%Y"),
            'slug': self.slug,
        })

    def __unicode__(self):
        return self.title
