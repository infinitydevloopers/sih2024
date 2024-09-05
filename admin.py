from django.contrib import admin
from .models import (
    Event, 
    EventParticipants, 
    Funding, 
    Innovation, 
    Investment, 
    IPR, 
    Mentorship, 
    Research, 
    Roll, 
    Startup, 
    StartupRole, 
    User
)

# Register your models herefrom django.contrib import admin
from .models import (
    User, Roll, Event, EventParticipants, Funding, Innovation,
    Investment, IPR, Mentorship, Research, Startup, StartupRole, UserRoll
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_no', 'updated_at', 'last_logged_in_at')
    search_fields = ('name', 'email')
    ordering = ('name',)
    list_filter = ('updated_at',)

@admin.register(Roll)
class RollAdmin(admin.ModelAdmin):
    list_display = ('roll_id', 'roll_name')
    search_fields = ('roll_name',)
    ordering = ('roll_name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'date', 'location', 'created_by', 'created_at')
    search_fields = ('event_name', 'location', 'created_by__name')
    ordering = ('-created_at',)
    list_filter = ('date', 'created_by')

@admin.register(EventParticipants)
class EventParticipantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user', 'role')
    search_fields = ('event__event_name', 'user__name', 'role')
    ordering = ('event', 'user')

@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = ('funding_id', 'startup', 'investor', 'amount', 'round', 'date')
    search_fields = ('startup__name', 'investor__name', 'amount', 'round')
    ordering = ('-date',)
    list_filter = ('round', 'date')

@admin.register(Innovation)
class InnovationAdmin(admin.ModelAdmin):
    list_display = ('innovation_id', 'title', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'status', 'associated_startup__name')
    ordering = ('-created_at',)
    list_filter = ('status', 'created_at')

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('investment_id', 'investment_type', 'entity', 'investor', 'amount', 'date')
    search_fields = ('investment_type', 'entity__title', 'investor__name', 'amount')
    ordering = ('-date',)
    list_filter = ('investment_type', 'date')

@admin.register(IPR)
class IPRAdmin(admin.ModelAdmin):
    list_display = ('ipr_id', 'ipr_type', 'title', 'status', 'file_date', 'granted_date', 'owner')
    search_fields = ('title', 'ipr_type', 'owner__name')
    ordering = ('-file_date',)
    list_filter = ('ipr_type', 'status')

@admin.register(Mentorship)
class MentorshipAdmin(admin.ModelAdmin):
    list_display = ('mentorship_id', 'mentor', 'mentee', 'start_date', 'end_date', 'status')
    search_fields = ('mentor__name', 'mentee__name', 'status')
    ordering = ('-start_date',)
    list_filter = ('status', 'start_date')

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('research_id', 'title', 'lead_researcher', 'status', 'start_date', 'end_date')
    search_fields = ('title', 'lead_researcher__name', 'status')
    ordering = ('-start_date',)
    list_filter = ('status', 'start_date')

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('startup_id', 'name', 'incorporation_date', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'status', 'related_innovation__title')
    ordering = ('-created_at',)
    list_filter = ('status', 'incorporation_date')

@admin.register(StartupRole)
class StartupRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'startup', 'user', 'startup_role')
    search_fields = ('startup__name', 'user__name', 'startup_role')
    ordering = ('startup', 'user')

@admin.register(UserRoll)
class UserRollAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'roll')
    search_fields = ('user__name', 'roll__roll_name')
    ordering = ('user', 'roll')



class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'location', 'created_by', 'created_at')
    search_fields = ('event_name', 'location', 'created_by__username')
    list_filter = ('date', 'location')

class EventParticipantsAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'role')
    search_fields = ('event__event_name', 'user__username', 'role')
    list_filter = ('role',)

class FundingAdmin(admin.ModelAdmin):
    list_display = ('startup', 'investor', 'amount', 'round', 'date')
    search_fields = ('startup__name', 'investor__username', 'round')
    list_filter = ('round', 'date')

class InnovationAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'associated_startup', 'created_at')
    search_fields = ('title', 'associated_startup__name', 'status')
    list_filter = ('status', 'created_at')

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('investment_type', 'entity', 'investor', 'amount', 'date')
    search_fields = ('entity', 'investor__username', 'investment_type')
    list_filter = ('investment_type', 'date')

class IPRAdmin(admin.ModelAdmin):
    list_display = ('ipr_type', 'title', 'application_number', 'registration_number', 'status', 'granted_date')
    search_fields = ('title', 'application_number', 'registration_number', 'owner__username')
    list_filter = ('ipr_type', 'status', 'granted_date')

class MentorshipAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'start_date', 'end_date', 'status')
    search_fields = ('mentor__username', 'mentee__username')
    list_filter = ('status', 'start_date', 'end_date')

class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'lead_researcher', 'status', 'start_date', 'end_date')
    search_fields = ('title', 'lead_researcher__username', 'status')
    list_filter = ('status', 'start_date', 'end_date')

class RollsAdmin(admin.ModelAdmin):
    list_display = ('roll_name',)
    search_fields = ('roll_name',)

class StartupAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'incorporation_date', 'created_at')
    search_fields = ('name', 'status')
    list_filter = ('status', 'incorporation_date')

class StartupRoleAdmin(admin.ModelAdmin):
    list_display = ('startup', 'user', 'startup_role')
    search_fields = ('startup__name', 'user__username', 'startup_role')
    list_filter = ('startup_role',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email', 'role__roll_name')
    list_filter = ('role__roll_name',)

# Register the models with the admin interface
admin.site.register(Event, EventAdmin)
admin.site.register(EventParticipants, EventParticipantsAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(Innovation, InnovationAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(IPR, IPRAdmin)
admin.site.register(Mentorship, MentorshipAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Roll, RollsAdmin)
admin.site.register(Startup, StartupAdmin)
admin.site.register(StartupRole, StartupRoleAdmin)
admin.site.register(User, UserAdmin)
