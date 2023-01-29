from django.contrib import admin
from .models import Petsitter

class PetsitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'zipcode', 'city', 'is_available_help', 'pet_type_take_care')
    

admin.site.register(Petsitter, PetsitterAdmin)