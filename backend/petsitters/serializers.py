from rest_framework import serializers
from .models import Petsitter

class PetsitterSerializer(serializers.ModelSerializer):

    class Meta:
        model=Petsitter
        fields=('pk', 'name', 'email', 'zipcode', 'city', 'is_available_help', 'pet_type_take_care', 'pets')
   