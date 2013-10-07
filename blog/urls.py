
from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
                           views.DetailsView.as_view(), name='details'),
                       url(r'^tags/(?P<slug>[-\w]+)/$', views.TagView.as_view(), name='tags'),
                       )
