from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from home import views, urls
import blog.views


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('home.urls')),
    url(r'^djplayer/', include('djplayer.urls', namespace="djplayer")),
    url(r'^discography/', include('discography.urls',
                                  namespace="discography")),
    url(r'^events/', include('events.urls', namespace="events")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),

    # Blog
    #url(r'^', include('blog.urls', namespace="blog")),
    url(r'^$', blog.views.IndexView.as_view(), name='index'),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^comments/', include('fluent_comments.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$',
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT,
                                  'show_indexes': True}),
                            )
