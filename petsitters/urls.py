from django.urls import path
from .views import petsitters_list, petsitters_detail, petsitters_detail_pets_list

#/petsitters/
urlpatterns = [
    path('', petsitters_list),
    path('<int:pk>/', petsitters_detail),
   
#petsitters/id/pets
    path('<int:pk>/pets/', petsitters_detail_pets_list)
    # path('<int:pk>/pets/<int:pk>', petsitters_detail_pets_detail)
]