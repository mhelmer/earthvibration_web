from django.conf.urls import patterns, url

from discography import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<year>\d{4})/(?P<slug>[-\w]+)/$',
                           views.ReleaseView.as_view(), name='release'),
                       url(r'^artist/(?P<slug>[-\w]+)/$',
                           views.ReleaseView.as_view(), name='artist'),
                       )
