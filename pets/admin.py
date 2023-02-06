from django.contrib import admin

# Register your models here.
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'petsitter', 'pet_name', 'pet_type_needs_care', 'pet_needs_description', 'is_needs_care')
    list_filter = ('id', 'is_needs_care')
    search_fields = ('is_needs_care',)


admin.site.register(Pet, PetAdmin)

