from django.db import models

# Create your models here.
class Petsitter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    zipcode = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, default="")
    is_available_help = models.BooleanField(default=False)
    pet_type_take_care = models.CharField(max_length=50)
    is_looking_for_help = models.BooleanField(default=False)
    photo_petsitter = models.ImageField(default="/images/blank-profile-picture.jpg",upload_to='images/')
    

    
    def __str__(self):
        return self.name
    
