from django.contrib import admin

# Register your models here.
from .models import User, Event, EventParticipants, Innovation, Investment, IPR, Research, Startup, Mentorship, Request

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'phone_no')

from django.contrib import admin
from .models import Investment
from .forms import InvestmentAdminForm

class InvestmentAdmin(admin.ModelAdmin):
    form = InvestmentAdminForm
    list_display = ('investment_id', 'investment_type', 'round', 'amount', 'date', 'entity', 'investor')

    class Media:
        js = ('admin/js/investment_admin.js',)  # Adjust the path if necessary

admin.site.register(Investment, InvestmentAdmin)


admin.site.register(Event)
admin.site.register(EventParticipants)
admin.site.register(Innovation)
# admin.site.register(Investment)
admin.site.register(IPR)
admin.site.register(Research)
admin.site.register(Startup)
admin.site.register(Mentorship)
admin.site.register(Request)
(Request)
