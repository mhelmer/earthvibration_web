from django.conf.urls import patterns, url

from gallery import views


urlpatterns = patterns('',
                       #url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<galleryslug>[-\w]+)/(?P<slug>[-\w]+)/$',
                           views.IndexView.as_view(), name='image'),
                       )
