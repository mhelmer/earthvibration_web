from django.db import models
import os


def get_file_path(instance, filename):
    return os.path.join('audio', str(instance.date_created.year),
                        str(instance.slug), 'mp3', filename)


class Tune(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField('slug', unique_for_year='date_published')
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_published = models.DateTimeField('date published')
    mp3_file = models.FileField(upload_to=get_file_path)
