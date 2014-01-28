from django.conf.urls import patterns, url

from gallery import views


urlpatterns = patterns('',
                       #url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^album/(?P<slug>[-\w]+)/$', views.AlbumView.as_view(),
                           name='album'),
                       url(r'^image/(?P<albumslug>[-\w]+)/(?P<slug>[-\w]+)/$',
                           views.ImageView.as_view(), name='image'),
                       url(r'^widget/(?P<slug>[-\w]+)/$',
                           views.AlbumView.as_view(
                               template_name='gallery/widget.html'),
                           name='widget'),
                       )
