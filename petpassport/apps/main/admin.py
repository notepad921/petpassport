from django.contrib import admin

from .models import *

# admin.site.register(Record)
admin.site.register(Pet)

admin.site.register(PetSex)
admin.site.register(PetTypes)
admin.site.register(Chip)
admin.site.register(Tattoo)
admin.site.register(Food)
admin.site.register(Accessory)
admin.site.register(EventsType)
admin.site.register(PetEvents)
admin.site.register(VaccinationType)
admin.site.register(Vaccination)
admin.site.register(CastrationStatus)
admin.site.register(Deworming)