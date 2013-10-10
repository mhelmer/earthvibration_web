from django.conf.urls import patterns, url

from djplayer import views


urlpatterns = patterns('',
                       url(r'^(?P<year>\d{4})/(?P<slug>[-\w]+)/$',
                           views.PlayerView.as_view(
                               template_name="djplayer/player.html"),
                           name='player'),
                       )
