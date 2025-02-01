from django.contrib import admin

from django.contrib import admin


from django.contrib import admin


from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('email','phone', 'purpose', 'scam_type', 'submitted_at')
    search_fields = ('email', 'phone')
    list_filter = ('purpose', 'scam_type', 'submitted_at')


from .models import ConsultationRequest

# Register the ConsultationRequest model with the admin site
admin.site.register(ConsultationRequest)


from django.contrib import admin
from .models import InvestmentData

admin.site.register(InvestmentData)
