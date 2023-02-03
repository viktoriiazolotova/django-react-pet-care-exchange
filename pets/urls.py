# from django.urls import path
# from .views import PetsView, PetView, SearchView

# #/pets/
# urlpatterns = [
#     path('', PetsView.as_view()),
#     path('<int:pk>',PetView.as_view()),
#     path('search', SearchView.as_view())

# ]
from django.urls import path
from .views import pets_list, pet_detail

#/petsitters/
urlpatterns = [
    path('', pets_list),
    path('<int:pk>/', pet_detail),
]