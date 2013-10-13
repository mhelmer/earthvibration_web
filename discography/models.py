from django.db import models
from sorl.thumbnail import ImageField
import os

from djplayer.models import Tune


def get_image_path(instance, filename):
    return os.path.join('releases', str(instance.release.release_date.year),
                        str(instance.release.slug), 'AlbumArt.jpg')


class Label(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Release(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField('slug', unique_for_year='release_date')
    release_date = models.DateTimeField('release date')
    catalog_number = models.CharField(max_length=20)
    published = models.BooleanField()
    tune = models.ForeignKey(Tune)
    label = models.ForeignKey(Label)

    class Meta:
        unique_together = ('label', 'catalog_number',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ''


class CoverImage(models.Model):
    release = models.ForeignKey(Release)
    image = ImageField(upload_to=get_image_path)
    kind = models.CharField(max_length=50)

    def __unicode__(self):
        return self.kind + ' image for ' + self.release.title


class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Track(models.Model):
    release = models.ForeignKey(Release)
    tracknum = models.CharField(max_length=10)
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.artist.name + ' - ' + self.title
