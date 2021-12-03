from django.contrib import admin
from .models import Drug, pd_prescriber, Credential, State, Triple, Prescriber_Credential
admin.site.register(Drug)
admin.site.register(pd_prescriber)
admin.site.register(Credential)
admin.site.register(State)
admin.site.register(Prescriber_Credential)
admin.site.register(Triple)
