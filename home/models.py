from django.db import models
from djplayer.models import Tune


class StudioMediaEntry(models.Model):
    create_date = models.DateTimeField('date created', auto_now_add=True)
    pub_date = models.DateTimeField('date published')
    tune = models.ForeignKey(Tune)
    content = models.TextField()

    def __unicode__(self):
        return self.tune.title
