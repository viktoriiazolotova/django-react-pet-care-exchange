from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('pk', 'petsitter', 'pet_name', 'pet_type_needs_care', 'pet_needs_description', 'is_needs_care', 'pet_photo')

class petDetailSerializer(serializers.ModelSerializer):
    model = Pet
    fields = '__all__'
    lookup_field = 'pk'