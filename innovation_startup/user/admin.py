from django.contrib import admin

# Register your models here.
from .models import User, Event, EventParticipants, Innovation, Investment, IPR, Research, Startup, Mentorship, Request

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'phone_no')



admin.site.register(Event)
admin.site.register(EventParticipants)
admin.site.register(Innovation)
admin.site.register(Investment)
admin.site.register(IPR)
admin.site.register(Research)
admin.site.register(Startup)
admin.site.register(Mentorship)
admin.site.register(Request)
