from django.db import models
import os


def get_image_path(instance, filename):
    return os.path.join('events', str(instance.id), 'flyer', filename)


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField('event date')
    description = models.TextField()
    location = models.CharField(max_length=200)
    admission = models.CharField(max_length=20)
    ageLimit = models.IntegerField(null=True)
    published = models.BooleanField()

    flyer = models.ImageField(upload_to=get_image_path, null=True,
                              blank=True)

    def flyer_tag(self):
        return u'<img src="%s" />' % self.flyer.url

    flyer_tag.short_description = 'Flyer'
    flyer_tag.allow_tags = True
