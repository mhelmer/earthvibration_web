from django.conf.urls import patterns, url

from djplayer import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<year>\d{4})/(?P<slug>[-\w]+)/$',
                           views.PlayerView.as_view(), name='player'),
                       )
