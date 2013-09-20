from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField('event date')
    description = models.TextField()
    location = models.CharField(max_length=200)
    admission = models.CharField(max_length=20)
    published = models.BooleanField()

    def __unicode__(self):
        return self.name

