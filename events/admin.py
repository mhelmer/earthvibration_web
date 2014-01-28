from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None, {'fields': ['date', 'description']}),
        (None, {'fields': ['location', 'admission', 'ageLimit', 'published']}),
        ('Flyer image', {'fields': ['flyer_tag'], 'classes': ['collapse']}),
        (None, {'fields': ['flyer']}),
    ]
    list_display = ('name', 'date', 'location')
    list_filter = ['date']
    search_fields = ['name', 'description']
    date_hierachy = 'date'
    readonly_fields = ('flyer_tag',)

admin.site.register(Event, EventAdmin)
