from django.conf.urls import patterns, url

from gallery import views


urlpatterns = patterns('',
                       #url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<albumslug>[-\w]+)/(?P<slug>[-\w]+)/$',
                           views.ImageView.as_view(), name='image'),
                       )
