from django.contrib import admin
from djplayer.models import Tune
from sorl.thumbnail.admin import AdminImageMixin


class TuneAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass

admin.site.register(Tune, TuneAdmin)
