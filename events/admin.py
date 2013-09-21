from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		('Date information', {'fields': ['date'], 'classes': ['collapse']}),
        ('Description', {'fields': ['description']}),
        (None, {'fields': ['location', 'admission', 'published']}),
	]
	list_display = ('name', 'date', 'location')
	list_filter = ['date']
	search_fields = ['name', 'description']
	date_hierachy = 'date'

admin.site.register(Event, EventAdmin)
