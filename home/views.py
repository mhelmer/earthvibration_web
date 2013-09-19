# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home/home.html"


class SoundsystemView(TemplateView):
    template_name = "home/soundsystem.html"


class StudioView(TemplateView):
    template_name = "home/studio.html"


class ReleasesView(TemplateView):
    template_name = "home/releases.html"


class MediaView(TemplateView):
    template_name = "home/media.html"


class ContactView(TemplateView):
    template_name = "home/contact.html"
