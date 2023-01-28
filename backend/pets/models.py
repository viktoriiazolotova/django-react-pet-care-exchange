from django.db import models

# Create your models here.
from petsitters.models import Petsitter

class Pet(models.Model):
    petsitter = models.ForeignKey(Petsitter, on_delete=models.CASCADE, related_name='pets')
    pet_name = models.CharField(max_length=50)
    pet_type_needs_care = models.CharField(max_length=50, default = 'other')
    # The default is blank=False. If blank=False, the field will be required.
    pet_needs_description = models.CharField(max_length=200, blank=True)
    is_needs_care = models.BooleanField(default=False)
    pet_photo = models.ImageField(upload_to='images/', default=None)


    def __str__(self):
        return self.pet_name
    
    
