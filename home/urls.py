from django.conf.urls import patterns, include, url

from home import views

urlpatterns = patterns('',
    url(r'^soundsystem/$', views.SoundsystemView.as_view(), name="soundsystem"),
    url(r'^studio/$', views.StudioView.as_view(), name="studio"),
    url(r'^releases/$', views.ReleasesView.as_view(), name="releases"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
)
