from django.contrib import admin
from .models import Organization, SystemUser, YoungSpecialistIndicators, MonthlyFormHeader, MonthlyFormLine

admin.site.register(Organization)
admin.site.register(SystemUser)
admin.site.register(YoungSpecialistIndicators)
admin.site.register(MonthlyFormHeader)
admin.site.register(MonthlyFormLine)
